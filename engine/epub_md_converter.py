#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import glob
import json
import argparse
import re
import concurrent.futures
from pathlib import Path
from datetime import datetime

try:
    import ebooklib
    import markdown
    import nltk
    # تلاش برای وارد کردن argcomplete
    try:
        import argcomplete
        HAS_ARGCOMPLETE = True
    except ImportError:
        HAS_ARGCOMPLETE = False
        print("هشدار: برای استفاده از قابلیت تکمیل خودکار، لطفاً argcomplete را نصب کنید:")
        print("pip install argcomplete")
        
    nltk.download('punkt', quiet=True)
except ImportError as e:
    module = str(e).split("'")[1]
    print(f"خطا: ماژول {module} نصب نشده است.")
    print(f"لطفاً با دستور زیر آن را نصب کنید:")
    print(f"pip install {module}")
    sys.exit(1)

# اضافه کردن مسیر پروژه به PYTHONPATH
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

# تعریف مسیر پایه در یک جای کد برای استفاده در همه جا
base_dir = Path(project_root).parent / "books"

try:
    from converters.epub_to_markdown import EpubToMarkdownConverter
    from converters.markdown_to_epub import MarkdownToEpubConverter
    from utils.file_manager import FileManager
except ImportError as e:
    print(f"خطا در وارد کردن ماژول‌ها: {e}")
    print("لطفاً مطمئن شوید که ساختار پروژه صحیح است.")
    sys.exit(1)

# ایجاد یک نمونه FileManager با base_dir که در همه جا استفاده می‌شود
file_manager = FileManager(base_dir)

def find_epub_files():
    """
    یافتن تمام فایل‌های EPUB موجود در مسیر پایه و زیرپوشه‌ها
    
    Returns:
        list: لیست نام کتاب‌ها (بدون پسوند)
    """
    epub_files = []
    
    # جستجو در مسیر پایه
    for epub_file in base_dir.glob("*.epub"):
        epub_files.append(epub_file.stem)
    
    # جستجو در مسیر دانلودها (اگر وجود داشته باشد)
    download_dir = Path(os.path.expanduser("~/Downloads"))
    if download_dir.exists():
        for epub_file in download_dir.glob("*.epub"):
            epub_files.append(epub_file.stem)
    
    # جستجو در زیرپوشه‌های کتاب
    for book_dir in base_dir.iterdir():
        if book_dir.is_dir():
            for epub_file in book_dir.glob("*.epub"):
                epub_files.append(epub_file.stem)
    
    return epub_files

def find_book_dirs():
    """
    یافتن تمام پوشه‌های کتاب موجود
    
    Returns:
        list: لیست نام پوشه‌های کتاب
    """
    book_dirs = []
    
    # پوشه‌های موجود در مسیر پایه
    for item in base_dir.iterdir():
        if item.is_dir() and not item.name.startswith('.') and item.name != 'engine':
            if (item / "en").exists() or (item / "fa").exists():
                book_dirs.append(item.name)
    
    return book_dirs

def book_completer(prefix, **kwargs):
    """
    تابع تکمیل خودکار برای نام‌های کتاب
    
    Args:
        prefix (str): بخش اولیه نام کتاب که کاربر تایپ کرده
        
    Returns:
        list: لیست کتاب‌هایی که با prefix شروع می‌شوند
    """
    all_books = set(find_epub_files() + find_book_dirs())
    return [b for b in all_books if b.startswith(prefix)]

#---------------------------- تبدیل EPUB به Markdown ----------------------------#

def process_book_to_md(book_name, min_words=150):
    """
    تبدیل یک کتاب EPUB به فایل‌های Markdown
    
    Args:
        book_name (str): نام کتاب (بدون پسوند)
        min_words (int): حداقل تعداد کلمات در هر فایل Markdown
    
    Returns:
        bool: True در صورت موفقیت، False در صورت شکست
    """
    try:
        # استفاده از نمونه سینگلتون FileManager
        paths = file_manager.get_book_paths(book_name)
        epub_path = paths["epub_path"]
        
        # بررسی وجود فایل EPUB اصلی
        if not epub_path.exists():
            # جستجوی فایل EPUB در مسیرهای دیگر
            alternative_paths = [
                base_dir / book_name / f"{book_name}.epub",                   # در پوشه کتاب
                Path(os.path.expanduser("~/Downloads")) / f"{book_name}.epub" # در دانلودها
            ]
            
            epub_found = False
            for alt_path in alternative_paths:
                if alt_path.exists():
                    epub_path = alt_path
                    epub_found = True
                    print(f"فایل EPUB در مسیر جایگزین یافت شد: {epub_path}")
                    break
            
            if not epub_found:
                print(f"خطا: فایل EPUB یافت نشد: {epub_path}")
                print("لطفاً فایل EPUB را در یکی از مسیرهای زیر قرار دهید:")
                print(f"1. {paths['epub_path']}")
                print(f"2. {base_dir / book_name / f'{book_name}.epub'}")
                print(f"3. {Path(os.path.expanduser('~/Downloads')) / f'{book_name}.epub'}")
                return False
        
        # ایجاد و استفاده از تبدیل‌کننده EPUB به Markdown
        # ارسال file_manager به کانورتر
        converter = EpubToMarkdownConverter(epub_path, min_words, file_manager)
        return converter.convert()
    
    except Exception as e:
        print(f"خطا در تبدیل EPUB به Markdown: {e}")
        return False

#---------------------------- تبدیل Markdown به EPUB ----------------------------#

def process_book_to_epub(book_name, language='fa', is_rtl=True):
    """
    تبدیل فایل‌های Markdown یک کتاب به EPUB
    
    Args:
        book_name (str): نام کتاب
        language (str): زبان کتاب (همیشه 'fa')
        is_rtl (bool): آیا متن از راست به چپ است (همیشه True)
    
    Returns:
        bool: True در صورت موفقیت، False در صورت شکست
    """
    try:
        # استفاده از نمونه سینگلتون FileManager
        paths = file_manager.get_book_paths(book_name)
        book_dir = paths["book_dir"]
        metadata_path = paths["metadata_path"]
        
        if not book_dir.exists():
            print(f"خطا: پوشه کتاب یافت نشد: {book_dir}")
            return False
        
        # ایجاد و استفاده از تبدیل‌کننده Markdown به EPUB
        concatenate = not metadata_path.exists()  # اگر متادیتا نباشد، فایل‌ها را ترکیب می‌کنیم
        
        # ارسال file_manager به کانورتر
        converter = MarkdownToEpubConverter(
            book_dir, 
            language=language, 
            file_manager=file_manager, 
            is_rtl=is_rtl, 
            concatenate=concatenate
        )
        return converter.convert()
    
    except Exception as e:
        print(f"خطا در تبدیل Markdown به EPUB: {e}")
        return False

def convert_to_kebab_case(name):
    """تبدیل نام به فرمت kebab-case
    
    Args:
        name (str): نام اصلی
        
    Returns:
        str: نام تبدیل شده به kebab-case
    """
    # حذف کاراکترهای خاص
    name = re.sub(r'[^\w\s-]', '', name.lower())
    # جایگزینی فاصله‌ها با خط تیره
    name = re.sub(r'[\s_]+', '-', name)
    return name

def main():
    """تابع اصلی برنامه"""
    parser = argparse.ArgumentParser(description="تبدیل کتاب بین فرمت‌های EPUB و Markdown")
    
    # ایجاد زیر پارسرها برای دستورات مختلف
    subparsers = parser.add_subparsers(dest='command', help='دستور اصلی')
    
    # دستور epub2md - تبدیل EPUB به Markdown
    epub2md_parser = subparsers.add_parser('epub2md', help='تبدیل EPUB به Markdown')
    epub2md_parser.add_argument('book_name', type=str, help='نام کتاب برای تبدیل').completer = book_completer
    epub2md_parser.add_argument('--min-words', type=int, default=150, help='حداقل تعداد کلمات در هر فایل Markdown')
    
    # دستور md2epub - تبدیل Markdown به EPUB
    md2epub_parser = subparsers.add_parser('md2epub', help='تبدیل Markdown به EPUB')
    md2epub_parser.add_argument('book_name', type=str, help='نام کتاب برای تبدیل').completer = book_completer
    
    # دستور list - نمایش لیست کتاب‌های موجود
    list_parser = subparsers.add_parser('list', help='نمایش لیست کتاب‌های موجود')
    
    # فعال‌سازی تکمیل خودکار اگر argcomplete موجود باشد
    if HAS_ARGCOMPLETE:
        argcomplete.autocomplete(parser)
    
    # تجزیه آرگومان‌ها
    args = parser.parse_args()
    
    # بررسی دستور
    if args.command == 'epub2md':
        # تبدیل EPUB به Markdown با استفاده از نام کتاب
        process_book_to_md(args.book_name, args.min_words)
    elif args.command == 'md2epub':
        # تبدیل Markdown به EPUB با استفاده از نام کتاب
        # زبان همیشه فارسی و RTL است
        process_book_to_epub(args.book_name)
    elif args.command == 'list':
        # نمایش لیست کتاب‌های موجود
        epub_files = find_epub_files()
        book_dirs = find_book_dirs()
        
        print("فایل‌های EPUB موجود:")
        for epub in epub_files:
            print(f"  - {epub}")
        
        print("\nپوشه‌های کتاب موجود:")
        for book_dir in book_dirs:
            print(f"  - {book_dir}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main() 
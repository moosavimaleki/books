#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path

# اضافه کردن مسیر پروژه به PYTHONPATH
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from utils.file_manager import FileManager
from models.metadata import Metadata, MetadataManager
from converters.epub_creator import EpubCreator

class MarkdownToEpubConverter:
    """کلاس مسئول تبدیل فایل‌های Markdown به EPUB"""
    
    def __init__(self, book_dir, language='en', file_manager=None, max_files=None, is_rtl=False, concatenate=False):
        """
        راه‌اندازی تبدیل‌کننده Markdown به EPUB
        
        Args:
            book_dir (str): مسیر پوشه کتاب
            language (str): زبان ('en' یا 'fa')
            file_manager (FileManager): نمونه FileManager سینگلتون
            max_files (int): حداکثر تعداد فایل‌ها برای پردازش
            is_rtl (bool): آیا متن از راست به چپ است؟
            concatenate (bool): آیا فایل‌ها در یک فصل ترکیب شوند؟
        """
        self.book_dir = Path(book_dir)
        self.language = language
        self.max_files = max_files
        self.is_rtl = is_rtl
        self.concatenate = concatenate
        
        # تعیین مسیر اصلی کتاب
        if self.book_dir.name in ['en', 'fa']:
            self.main_dir = self.book_dir.parent
            self.book_name = self.main_dir.name
        else:
            self.main_dir = self.book_dir
            self.book_name = self.main_dir.name
        
        self.file_manager = file_manager
        
        # دریافت مسیرها از FileManager
        self.paths = self.file_manager.get_book_paths(self.book_name)
        
        # تنظیم مسیرها
        self.md_dir = self.paths[f"{language}_dir"]
        
        # تنظیم جهت متن
        if language == 'fa':
            self.is_rtl = True
            
        # ایجاد مدیریت‌کننده‌ها
        self.metadata_manager = MetadataManager(self.main_dir, file_manager=self.file_manager)
        self.epub_creator = EpubCreator(book_dir, language, is_rtl=self.is_rtl, file_manager=self.file_manager)
        
    def convert(self):
        """
        تبدیل فایل‌های Markdown به EPUB
        
        Returns:
            bool: True در صورت موفقیت، False در صورت شکست
        """
        # بررسی وجود پوشه Markdown
        if not self.md_dir.exists():
            print(f"خطا: پوشه Markdown یافت نشد: {self.md_dir}")
            return False
        
        # بررسی وجود فایل‌های Markdown
        md_files = self.file_manager.get_markdown_files(
            lang=self.language, 
            max_files=self.max_files,
            book_name=self.book_name
        )
        if not md_files:
            print(f"خطا: هیچ فایل Markdown در {self.md_dir} یافت نشد!")
            return False
        
        print(f"تبدیل فایل‌های Markdown در {self.md_dir}...")
        print(f"زبان: {self.language} ({'راست به چپ' if self.is_rtl else 'چپ به راست'})")
        print(f"تعداد فایل‌های Markdown یافت شده: {len(md_files)}")
        
        # بارگذاری متادیتا
        metadata = self.metadata_manager.get_metadata()
        if metadata:
            print(f"متادیتا بارگذاری شد: عنوان کتاب - {metadata.title}")
            print(f"تعداد فصل‌ها در متادیتا: {len(metadata.chapters)}")
            # تنظیم متادیتا در epub_creator
            self.epub_creator.metadata = metadata
        else:
            print("هشدار: متادیتا یافت نشد، ایجاد کتاب بدون متادیتا...")
        
        # آماده‌سازی کتاب EPUB
        self.epub_creator.prepare_book()
        
        # افزودن تصاویر به EPUB
        self.epub_creator.add_images()
        
        # پردازش فایل‌های Markdown
        self.epub_creator.process_markdown_files(md_files, self.concatenate)
        
        # نهایی‌سازی و ذخیره کتاب
        success = self.epub_creator.finalize_book()
        
        if success:
            output_file = self.paths["output_epub_path"]
            print(f"تبدیل به EPUB با موفقیت انجام شد: {output_file}")
            return True
        else:
            print("خطا در ایجاد فایل EPUB!")
            return False
    
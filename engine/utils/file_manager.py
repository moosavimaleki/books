#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import shutil
from pathlib import Path

class FileManager:
    """کلاس مسئول مدیریت پوشه‌ها و فایل‌ها برای کتاب (سینگلتون)"""
    
    _instance = None
    
    def __new__(cls, base_dir=None):
        """
        ایجاد یا بازگرداندن نمونه موجود از FileManager (الگوی سینگلتون)
        
        Args:
            base_dir (str): مسیر پایه برای کتاب (فقط در اولین فراخوانی مورد استفاده قرار می‌گیرد)
        """
        if cls._instance is None:
            if base_dir is None:
                raise ValueError("base_dir باید در اولین فراخوانی مشخص شود")
            cls._instance = super(FileManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, base_dir=None):
        """
        راه‌اندازی مدیر فایل
        
        Args:
            base_dir (str): مسیر پایه برای کتاب
        """
        if not self._initialized:
            if base_dir is None:
                raise ValueError("base_dir نمی‌تواند خالی باشد")
            self.base_dir = Path(base_dir)
            self._initialized = True
    
    def get_book_paths(self, book_name):
        """
        دریافت مسیرهای پوشه‌ها و فایل‌های مربوط به یک کتاب
        
        Args:
            book_name (str): نام کتاب
            
        Returns:
            dict: دیکشنری از مسیرهای کتاب
        """
        # مسیر اصلی کتاب
        book_dir = self.base_dir / book_name
        
        # مسیرهای فرعی
        images_dir = book_dir / "images"
        en_dir = book_dir / "en"
        fa_dir = book_dir / "fa"
        
        # مسیرهای فایل‌ها
        epub_path = self.base_dir / f"{book_name}.epub"
        output_epub_path = book_dir / f"{book_name}_converted.epub"
        metadata_path = book_dir / "metadata.json"
        
        return {
            "book_dir": book_dir,
            "images_dir": images_dir,
            "en_dir": en_dir,
            "fa_dir": fa_dir,
            "epub_path": epub_path,
            "output_epub_path": output_epub_path,
            "metadata_path": metadata_path
        }
    
    def ensure_dir_exists(self, dir_path):
        """
        اطمینان از وجود یک دایرکتوری، در صورت عدم وجود آن را ایجاد می‌کند
        
        Args:
            dir_path (str یا Path): مسیر دایرکتوری مورد نظر
            
        Returns:
            Path: مسیر ایجاد شده
        """
        dir_path = Path(dir_path)
        os.makedirs(dir_path, exist_ok=True)
        return dir_path
    
    def create_book_structure(self, book_name):
        """
        ایجاد ساختار پوشه‌های استاندارد برای یک کتاب
        
        Args:
            book_name (str): نام کتاب
            
        Returns:
            dict: دیکشنری از مسیرهای ایجاد شده
        """
        # مسیر اصلی کتاب
        book_dir = self.base_dir / book_name
        self.ensure_dir_exists(book_dir)
        
        # مسیرهای فرعی
        images_dir = book_dir / "images"
        en_dir = book_dir / "en"
        fa_dir = book_dir / "fa"
        
        # ایجاد دایرکتوری‌ها
        self.ensure_dir_exists(images_dir)
        self.ensure_dir_exists(en_dir)
        self.ensure_dir_exists(fa_dir)
        
        return {
            "book_dir": book_dir,
            "images_dir": images_dir,
            "en_dir": en_dir,
            "fa_dir": fa_dir
        }
    
    def clean_filename(self, filename):
        """
        پاکسازی نام فایل برای اطمینان از مجاز بودن کاراکترها
        
        Args:
            filename (str): نام فایل اصلی
            
        Returns:
            str: نام فایل پاکسازی شده
        """
        # حذف کاراکترهای غیرمجاز در نام فایل
        invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
        for char in invalid_chars:
            filename = filename.replace(char, '_')
        return filename
    
    def write_markdown_file(self, content, filename, lang='en', book_name=None):
        """
        نوشتن محتوا در یک فایل Markdown
        
        Args:
            content (str): محتوای Markdown
            filename (str): نام فایل
            lang (str): زبان ('en' یا 'fa')
            book_name (str): نام کتاب (اختیاری)
            
        Returns:
            str: مسیر کامل فایل نوشته شده
        """
        if book_name:
            # اگر book_name مشخص شده باشد، از آن برای محاسبه مسیر استفاده می‌کنیم
            paths = self.get_book_paths(book_name)
            lang_dir = paths[f"{lang}_dir"]
        else:
            # اگر مشخص نشده باشد، از مسیر فعلی استفاده می‌کنیم (برای همسازگاری با کد قبلی)
            lang_dir = self.ensure_dir_exists(f"{self.base_dir.name}/{lang}")
        
        clean_name = self.clean_filename(filename)
        file_path = lang_dir / clean_name
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return str(file_path)
    
    def read_markdown_file(self, filename, lang='en'):
        """
        خواندن محتوای یک فایل Markdown
        
        Args:
            filename (str): نام فایل
            lang (str): زبان ('en' یا 'fa')
            
        Returns:
            str: محتوای فایل یا None در صورت بروز خطا
        """
        try:
            file_path = self.base_dir / lang / filename
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"خطا در خواندن فایل {filename}: {e}")
            return None
    
    def get_markdown_files(self, lang='en', max_files=None, book_name=None):
        """
        دریافت لیست فایل‌های Markdown در یک زبان خاص
        
        Args:
            lang (str): زبان ('en' یا 'fa')
            max_files (int): حداکثر تعداد فایل‌ها برای بازگرداندن
            book_name (str): نام کتاب (اختیاری)
            
        Returns:
            list: لیستی از مسیرهای فایل‌های Markdown
        """
        # گزارش مسیر پایه برای کمک به دیباگ
        print(f"DEBUG: جستجوی فایل‌های {lang} برای کتاب {book_name}")
        
        if book_name:
            # اگر book_name داده شده، از get_book_paths استفاده کنیم
            book_paths = self.get_book_paths(book_name)
            lang_dir = book_paths[f"{lang}_dir"]
        else:
            # روش قدیمی اگر book_name مشخص نشده باشد
            lang_dir = self.base_dir / lang
            
        print(f"DEBUG: مسیر جستجوی فایل‌ها: {lang_dir}")
        
        if not lang_dir.exists():
            print(f"مسیر {lang_dir} وجود ندارد!")
            return []
            
        md_files = sorted(lang_dir.glob("*.md"))
        
        if max_files:
            md_files = md_files[:int(max_files)]
            
        return [str(f) for f in md_files]
    
    def save_image(self, image_data, image_name, book_name=None):
        """
        ذخیره یک تصویر در پوشه تصاویر
        
        Args:
            image_data (bytes): داده‌های باینری تصویر
            image_name (str): نام فایل تصویر
            book_name (str): نام کتاب (اختیاری)
            
        Returns:
            str: مسیر نسبی تصویر ذخیره شده
        """
        if book_name:
            # اگر book_name مشخص شده باشد، از آن برای محاسبه مسیر استفاده می‌کنیم
            paths = self.get_book_paths(book_name)
            images_dir = paths["images_dir"]
        else:
            # اگر مشخص نشده باشد، از مسیر فعلی استفاده می‌کنیم (برای همسازگاری با کد قبلی)
            images_dir = self.ensure_dir_exists(f"{self.base_dir.name}/images")
        
        clean_name = self.clean_filename(image_name)
        image_path = images_dir / clean_name
        
        with open(image_path, 'wb') as f:
            f.write(image_data)
        
        # مسیر نسبی نسبت به پوشه زبان برمی‌گرداند
        return f"../images/{clean_name}"
    
    def get_images(self):
        """
        دریافت لیست تمام تصاویر موجود
        
        Returns:
            list: لیستی از مسیرهای تصاویر
        """
        images_dir = self.base_dir / "images"
        if not images_dir.exists():
            return []
            
        image_extensions = ["*.jpg", "*.jpeg", "*.png", "*.gif", "*.svg"]
        images = []
        
        for ext in image_extensions:
            images.extend(images_dir.glob(ext))
            
        return [str(img) for img in images]
        
    def count_files(self, pattern, book_name=None):
        """
        شمارش تعداد فایل‌های موجود با یک الگوی خاص
        
        Args:
            pattern (str): الگوی جستجو
            book_name (str): نام کتاب (اختیاری)
            
        Returns:
            int: تعداد فایل‌های یافت شده
        """
        # گزارش مسیر پایه برای کمک به دیباگ
        print(f"DEBUG: مسیر پایه: {self.base_dir}")
        
        paths_to_try = []
        
        # اگر book_name داده شده، از get_book_paths استفاده کنیم
        if book_name:
            book_paths = self.get_book_paths(book_name)
            
            # الگو را بررسی کنیم تا مسیر مناسب را انتخاب کنیم
            if pattern == 'en/*.md' or pattern.startswith('en/'):
                # فایل‌های انگلیسی
                path_pattern = str(book_paths["en_dir"] / pattern.replace('en/', ''))
                paths_to_try.append(path_pattern)
            elif pattern == 'fa/*.md' or pattern.startswith('fa/'):
                # فایل‌های فارسی
                path_pattern = str(book_paths["fa_dir"] / pattern.replace('fa/', ''))
                paths_to_try.append(path_pattern)
            elif pattern == 'images/*' or pattern.startswith('images/'):
                # تصاویر
                path_pattern = str(book_paths["images_dir"] / pattern.replace('images/', ''))
                paths_to_try.append(path_pattern)
            else:
                # سایر الگوها
                path_pattern = str(book_paths["book_dir"] / pattern)
                paths_to_try.append(path_pattern)
                
            # گزارش مسیر نهایی برای کمک به دیباگ
            print(f"DEBUG: الگوی {book_name}/{pattern} -> {path_pattern}")
        else:
            # اگر book_name مشخص نشده، از روش‌های قبلی استفاده کنیم
            
            # روش ۱: بررسی اگر الگو با نام کتاب شروع می‌شود
            if '/' in pattern and not pattern.startswith('/'):
                book_name_from_pattern = pattern.split('/')[0]
                if book_name_from_pattern:
                    # سعی کنیم از get_book_paths استفاده کنیم
                    paths_to_try.append(self.base_dir / pattern)
            
            # روش ۲: افزودن مسیر کتاب به الگو
            paths_to_try.append(self.base_dir / pattern)
            
            # روش ۳: بررسی مستقیم فایل‌ها با استفاده از glob
            if "en/*.md" in pattern or pattern == "*.md":
                for subdir in self.base_dir.iterdir():
                    if subdir.is_dir() and (subdir / "en").exists():
                        paths_to_try.append(subdir / "en" / "*.md")
        
        # بررسی تمام مسیرها
        for path in paths_to_try:
            full_pattern = str(path)
            files = glob.glob(full_pattern)
            print(f"DEBUG: الگوی {full_pattern} -> {len(files)} فایل")
            
            if files:
                return len(files)
        
        # اگر هیچ فایلی پیدا نشد، صفر برگردان
        return 0 
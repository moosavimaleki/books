#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
from pathlib import Path
from datetime import datetime

class Metadata:
    """کلاس مدل برای نگهداری و دستکاری متادیتای کتاب"""
    
    def __init__(self, 
                 title=None, 
                 creator=None, 
                 language=None, 
                 original_file=None, 
                 creation_date=None,
                 direction=None,
                 chapters=None):
        """
        راه‌اندازی یک نمونه از متادیتا
        
        Args:
            title (str): عنوان کتاب
            creator (str): نویسنده یا ایجاد کننده کتاب
            language (str): زبان اصلی کتاب
            original_file (str): مسیر فایل EPUB اصلی
            creation_date (str): تاریخ ایجاد
            direction (str): جهت متن (rtl یا ltr)
            chapters (list): لیستی از اطلاعات فصل‌ها
        """
        self.title = title
        self.creator = creator
        self.language = language
        self.original_file = original_file
        self.creation_date = creation_date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.direction = direction or "ltr"
        self.chapters = chapters or []
        
    def add_chapter(self, md_file, title, html_file=None, order=None):
        """
        افزودن اطلاعات یک فصل به متادیتا
        
        Args:
            md_file (str): نام فایل Markdown
            title (str): عنوان فصل
            html_file (str): نام فایل HTML در EPUB اصلی
            order (int): ترتیب فصل در کتاب
        """
        if order is None:
            order = len(self.chapters) + 1
            
        chapter_info = {
            "md_file": md_file,
            "title": title,
            "order": order
        }
        
        if html_file:
            chapter_info["html_file"] = html_file
            
        self.chapters.append(chapter_info)
    
    def to_dict(self):
        """
        تبدیل متادیتا به دیکشنری برای ذخیره‌سازی
        
        Returns:
            dict: دیکشنری حاوی اطلاعات متادیتا
        """
        return {
            "title": self.title,
            "creator": self.creator,
            "language": self.language,
            "original_file": self.original_file,
            "creation_date": self.creation_date,
            "direction": self.direction,
            "chapters": self.chapters
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        ایجاد نمونه Metadata از یک دیکشنری
        
        Args:
            data (dict): دیکشنری حاوی اطلاعات متادیتا
            
        Returns:
            Metadata: نمونه ایجاد شده از متادیتا
        """
        metadata = cls(
            title=data.get("title"),
            creator=data.get("creator"),
            language=data.get("language"),
            original_file=data.get("original_file"),
            creation_date=data.get("creation_date"),
            direction=data.get("direction"),
        )
        
        metadata.chapters = data.get("chapters", [])
        return metadata


class MetadataManager:
    """مدیریت متادیتای کتاب"""
    
    def __init__(self, book_dir, file_manager=None):
        """
        راه‌اندازی مدیریت‌کننده متادیتا
        
        Args:
            book_dir (str): مسیر پوشه کتاب
            file_manager (FileManager): نمونه FileManager سینگلتون
        """
        self.book_dir = Path(book_dir)
        
        # استفاده از FileManager برای دریافت مسیرها
        if file_manager:
            self.file_manager = file_manager
            book_name = self.book_dir.name
            paths = self.file_manager.get_book_paths(book_name)
            self.metadata_file = paths["metadata_path"]
        else:
            # حالت پشتیبانی برای کد قدیمی
            self.metadata_file = self.book_dir / "metadata.json"
    
    def save_metadata(self, metadata):
        """
        ذخیره متادیتا در فایل JSON
        
        Args:
            metadata (Metadata): نمونه متادیتا برای ذخیره‌سازی
            
        Returns:
            bool: True اگر با موفقیت ذخیره شد، در غیر این صورت False
        """
        try:
            with open(self.metadata_file, 'w', encoding='utf-8') as f:
                json.dump(metadata.to_dict(), f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"خطا در ذخیره متادیتا: {e}")
            return False
    
    def load_metadata(self):
        """
        بارگیری متادیتا از فایل JSON
        
        Returns:
            Metadata: نمونه متادیتا بارگیری شده یا None در صورت بروز خطا
        """
        if not self.metadata_file.exists():
            print(f"فایل متادیتا یافت نشد: {self.metadata_file}")
            return None
            
        try:
            with open(self.metadata_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return Metadata.from_dict(data)
        except Exception as e:
            print(f"خطا در بارگیری متادیتا: {e}")
            return None
    
    def get_metadata(self):
        """
        بارگیری متادیتا از فایل JSON (نام دیگر برای load_metadata)
        
        Returns:
            Metadata: نمونه متادیتا بارگیری شده یا None در صورت بروز خطا
        """
        return self.load_metadata()
    
    def create_empty_metadata(self, title=None, creator=None, language=None):
        """
        ایجاد یک فایل متادیتای خالی
        
        Args:
            title (str): عنوان کتاب
            creator (str): نویسنده کتاب
            language (str): زبان کتاب
            
        Returns:
            Metadata: نمونه متادیتای جدید
        """
        metadata = Metadata(
            title=title or self.book_dir.name,
            creator=creator,
            language=language or "en"
        )
        
        self.save_metadata(metadata)
        return metadata 
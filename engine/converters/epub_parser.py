#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
import ebooklib
from ebooklib import epub

class EpubParser:
    """کلاس مسئول تجزیه و تحلیل فایل‌های EPUB و استخراج محتوای آن‌ها"""
    
    def __init__(self, epub_path):
        """
        راه‌اندازی پارسر EPUB
        
        Args:
            epub_path (str): مسیر فایل EPUB
        """
        self.epub_path = Path(epub_path)
        self.book = None
        self.metadata = {}
        self.chapters = []
        self.images = []
        
    def load(self):
        """
        بارگیری و تجزیه فایل EPUB
        
        Returns:
            bool: True در صورت موفقیت، False در صورت شکست
        """
        try:
            self.book = epub.read_epub(self.epub_path)
            self._extract_metadata()
            self._extract_chapters()
            self._extract_images()
            return True
        except Exception as e:
            print(f"خطا در بارگیری EPUB: {e}")
            return False
    
    def _extract_metadata(self):
        """استخراج متادیتای EPUB"""
        if not self.book:
            return
            
        # استخراج عنوان
        title = self.book.get_metadata('DC', 'title')
        if title:
            self.metadata['title'] = title[0][0]
        else:
            self.metadata['title'] = self.epub_path.stem
        
        # استخراج نویسنده
        creator = self.book.get_metadata('DC', 'creator')
        if creator:
            self.metadata['creator'] = creator[0][0]
        
        # استخراج زبان
        language = self.book.get_metadata('DC', 'language')
        if language:
            self.metadata['language'] = language[0][0]
            
        # تنظیم جهت متن
        rtl_languages = ['fa', 'ar', 'he', 'ur']
        lang_code = self.metadata.get('language', '').split('-')[0].lower()
        self.metadata['direction'] = 'rtl' if lang_code in rtl_languages else 'ltr'
        
        # ذخیره نام فایل اصلی
        self.metadata['original_file'] = str(self.epub_path)
    
    def _extract_chapters(self):
        """استخراج فصل‌های EPUB"""
        if not self.book:
            return
            
        # استخراج محتوای HTML از تمام بخش‌های کتاب
        items = list(self.book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
        
        # مرتب‌سازی بر اساس اسپاین (ترتیب فصل‌ها در کتاب)
        spine_ids = [item[0] for item in self.book.spine]
        
        # تعیین ترتیب صحیح فصل‌ها
        ordered_items = []
        for spine_id in spine_ids:
            for item in items:
                if item.id == spine_id:
                    ordered_items.append(item)
                    break
        
        # اضافه کردن هر آیتم باقیمانده که در اسپاین نیست
        for item in items:
            if item not in ordered_items:
                ordered_items.append(item)
        
        # استخراج عنوان و محتوای HTML از هر فصل
        for i, item in enumerate(ordered_items):
            html_content = item.get_content().decode('utf-8')
            file_name = item.get_name()
            
            # استخراج عنوان فصل
            title = self._extract_title(html_content) or f"Chapter {i+1}"
            
            # ذخیره اطلاعات فصل
            self.chapters.append({
                'id': item.id,
                'title': title,
                'file_name': file_name,
                'html_content': html_content,
                'order': i + 1
            })
    
    def _extract_title(self, html_content):
        """استخراج عنوان از محتوای HTML
        
        Args:
            html_content (str): محتوای HTML
            
        Returns:
            str: عنوان استخراج شده یا None
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # بررسی تگ‌های h1
        h1 = soup.find('h1')
        if h1 and h1.text.strip():
            return h1.text.strip()
        
        # بررسی تگ‌های h2
        h2 = soup.find('h2')
        if h2 and h2.text.strip():
            return h2.text.strip()
        
        # بررسی عنوان‌های با کلاس خاص
        title_classes = ['title', 'chapter-title', 'heading']
        for class_name in title_classes:
            title_elem = soup.find(class_=class_name)
            if title_elem and title_elem.text.strip():
                return title_elem.text.strip()
        
        return None
    
    def _extract_images(self):
        """استخراج تصاویر از EPUB"""
        if not self.book:
            return
            
        # استخراج تمام تصاویر از کتاب
        image_items = list(self.book.get_items_of_type(ebooklib.ITEM_IMAGE))
        
        for item in image_items:
            # ذخیره اطلاعات تصویر
            self.images.append({
                'id': item.id,
                'file_name': item.get_name(),
                'content': item.get_content(),
                'media_type': item.media_type
            })
    
    def extract_text_from_html(self, html_content):
        """استخراج متن خام از محتوای HTML
        
        Args:
            html_content (str): محتوای HTML
            
        Returns:
            str: متن خام
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # حذف تگ‌های script و style
        for script in soup(["script", "style"]):
            script.extract()
        
        # استخراج متن
        text = soup.get_text()
        
        # حذف خطوط خالی اضافی
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text
    
    def convert_html_to_markdown(self, html_content):
        """تبدیل محتوای HTML به Markdown با حفظ فرمت‌های مهم
        
        Args:
            html_content (str): محتوای HTML
            
        Returns:
            str: محتوای Markdown
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # حذف تگ‌های script و style
        for script in soup(["script", "style"]):
            script.extract()
        
        # پردازش تصاویر
        for img in soup.find_all('img'):
            if img.get('src'):
                alt_text = img.get('alt', '')
                markdown_img = f"![{alt_text}]({img['src']})"
                img.replace_with(BeautifulSoup(markdown_img, 'html.parser'))
        
        # پردازش لینک‌ها
        for a in soup.find_all('a'):
            if a.get('href'):
                link_text = a.get_text()
                markdown_link = f"[{link_text}]({a['href']})"
                a.replace_with(BeautifulSoup(markdown_link, 'html.parser'))
        
        # پردازش عناوین
        for i in range(1, 7):
            for header in soup.find_all(f'h{i}'):
                header_text = header.get_text()
                markdown_header = '#' * i + ' ' + header_text
                header.replace_with(BeautifulSoup(f"\n\n{markdown_header}\n\n", 'html.parser'))
        
        # پردازش پاراگراف‌ها
        for p in soup.find_all('p'):
            p_text = p.get_text()
            p.replace_with(BeautifulSoup(f"\n\n{p_text}\n\n", 'html.parser'))
        
        # پردازش لیست‌ها
        for ul in soup.find_all('ul'):
            items = []
            for li in ul.find_all('li'):
                items.append(f"* {li.get_text()}")
            ul.replace_with(BeautifulSoup("\n" + "\n".join(items) + "\n", 'html.parser'))
        
        for ol in soup.find_all('ol'):
            items = []
            for i, li in enumerate(ol.find_all('li')):
                items.append(f"{i+1}. {li.get_text()}")
            ol.replace_with(BeautifulSoup("\n" + "\n".join(items) + "\n", 'html.parser'))
        
        # پردازش تأکیدها (بولد و ایتالیک)
        for strong in soup.find_all(['strong', 'b']):
            text = strong.get_text()
            strong.replace_with(BeautifulSoup(f"**{text}**", 'html.parser'))
        
        for em in soup.find_all(['em', 'i']):
            text = em.get_text()
            em.replace_with(BeautifulSoup(f"*{text}*", 'html.parser'))
        
        # پردازش کدها
        for code in soup.find_all('code'):
            text = code.get_text()
            code.replace_with(BeautifulSoup(f"`{text}`", 'html.parser'))
        
        for pre in soup.find_all('pre'):
            text = pre.get_text()
            pre.replace_with(BeautifulSoup(f"```\n{text}\n```", 'html.parser'))
        
        # پردازش جداول
        for table in soup.find_all('table'):
            # فعلاً حفظ ساختار جدول
            pass
        
        # استخراج متن نهایی
        markdown_text = soup.get_text()
        
        # پاکسازی نهایی
        markdown_text = re.sub(r'\n{3,}', '\n\n', markdown_text)  # حذف خطوط خالی اضافی
        
        return markdown_text 
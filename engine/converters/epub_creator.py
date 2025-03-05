#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import markdown
from pathlib import Path
from bs4 import BeautifulSoup
import ebooklib
from ebooklib import epub

# استفاده از import مطلق به جای نسبی
import sys
import os.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.metadata import Metadata, MetadataManager

class EpubCreator:
    """کلاس مسئول ساخت فایل EPUB از فایل‌های Markdown"""
    
    def __init__(self, book_dir, language='en', is_rtl=False, file_manager=None):
        """
        راه‌اندازی سازنده EPUB
        
        Args:
            book_dir (str): مسیر پوشه کتاب
            language (str): زبان کتاب ('en' یا 'fa')
            is_rtl (bool): آیا متن از راست به چپ است؟
            file_manager (FileManager): نمونه FileManager سینگلتون
        """
        self.book_dir = Path(book_dir)
        self.language = language
        self.is_rtl = is_rtl
        
        # تنظیم مسیرها
        if self.book_dir.name in ['en', 'fa']:
            self.main_dir = self.book_dir.parent
            self.md_dir = self.book_dir
        else:
            self.main_dir = self.book_dir
            # استفاده از paths به جای عملگر /
            book_name = self.main_dir.name
            
            self.file_manager = file_manager
            
            self.paths = self.file_manager.get_book_paths(book_name)
            
            # استفاده از مسیرهای دریافت شده از get_book_paths
            self.md_dir = self.paths[f"{language}_dir"]
            self.images_dir = self.paths["images_dir"]
            self.output_file = self.paths["output_epub_path"]
        
        # بارگیری متادیتا
        self.metadata_manager = MetadataManager(self.main_dir, file_manager=self.file_manager)
        self.metadata = self.metadata_manager.load_metadata()
        
        # ایجاد کتاب EPUB جدید
        self.book = epub.EpubBook()
        self.chapters = []
        self.toc = []
        
    def prepare_book(self):
        """آماده‌سازی کتاب EPUB با متادیتا و استایل‌ها"""
        print(f"DEBUG: در prepare_book - مقدار is_rtl: {self.is_rtl}, زبان: {self.language}")
        
        if not self.metadata:
            print("هشدار: متادیتا یافت نشد. از مقادیر پیش‌فرض استفاده می‌شود.")
            self.metadata = Metadata(
                title=self.main_dir.name,
                language=self.language,
                direction="rtl" if self.is_rtl else "ltr"
            )
        
        # تنظیم متادیتای EPUB
        self.book.set_title(self.metadata.title or self.main_dir.name)
        
        if self.metadata.creator:
            self.book.add_author(self.metadata.creator)
        
        self.book.set_language(self.language)
        
        # تنظیم جهت متن
        direction = "rtl" if self.is_rtl else "ltr"
        print(f"DEBUG: تنظیم جهت متن به {direction} بر اساس is_rtl={self.is_rtl}")
        
        # افزودن فونت فارسی zar برای متن‌های راست به چپ
        if self.is_rtl:
            print("DEBUG: متن راست به چپ تشخیص داده شد، افزودن فونت فارسی...")
            try:
                self.add_font()
            except Exception as e:
                print(f"ERROR در add_font: {e}")
                import traceback
                traceback.print_exc()
        
        # افزودن CSS برای کتاب
        style = """
        @namespace epub "http://www.idpf.org/2007/ops";
        
        @font-face {
            font-family: 'Zar';
            src: url('../fonts/BZar.ttf');
            font-weight: normal;
            font-style: normal;
        }
        
        @font-face {
            font-family: 'Zar';
            src: url('../fonts/BZar-Bold.ttf');
            font-weight: bold;
            font-style: normal;
        }
        
        body {
            direction: rtl;
            text-align: right;
            font-family: 'Zar', 'Tahoma', sans-serif;
            line-height: 1.5;
        }
        h1, h2, h3, h4, h5, h6 {
            text-align: right;
            font-family: 'Zar', 'Tahoma', sans-serif;
            font-weight: bold;
        }
        """
        
        css = epub.EpubItem(
            uid="style_default",
            file_name="style/default.css",
            media_type="text/css",
            content=style
        )
        self.book.add_item(css)
    
    def add_images(self):
        """افزودن تصاویر به EPUB"""
        if not self.images_dir.exists():
            print(f"هشدار: پوشه تصاویر یافت نشد: {self.images_dir}")
            return
        
        # پوشه‌های احتمالی تصاویر
        possible_image_dirs = {
            'assets': Path(self.book_dir) / "assets",
            'graphics': Path(self.book_dir) / "graphics",
            'images': self.images_dir
        }
        
        # چک کردن پوشه‌های موجود
        valid_image_dirs = {}
        for dir_name, dir_path in possible_image_dirs.items():
            if dir_path.exists():
                print(f"DEBUG: پوشه {dir_name} در {dir_path} یافت شد")
                valid_image_dirs[dir_name] = dir_path
            else:
                print(f"DEBUG: پوشه {dir_name} در {dir_path} یافت نشد")
        
        # اگر پوشه اصلی یافت نشد، از images استفاده می‌کنیم
        if not valid_image_dirs:
            print("هشدار: هیچ پوشه تصویری یافت نشد. ادامه بدون تصاویر.")
            return
        
        image_count = 0
        image_extensions = ['jpg', 'jpeg', 'png', 'gif', 'svg']
        
        # دیکشنری برای ذخیره اطلاعات تمام تصاویر پردازش شده
        processed_images = {}
        
        # اضافه کردن تصاویر از تمام پوشه‌های معتبر
        for dir_name, dir_path in valid_image_dirs.items():
            # پردازش تصاویر در ریشه پوشه
            for ext in image_extensions:
                for img_path in dir_path.glob(f"*.{ext}"):
                    try:
                        with open(img_path, 'rb') as f:
                            image_content = f.read()
                        
                        # تعیین نوع رسانه
                        media_type = f"image/{ext}"
                        if ext == 'jpg':
                            media_type = "image/jpeg"
                        elif ext == 'svg':
                            media_type = "image/svg+xml"
                        
                        # تعیین مسیر تصویر در EPUB
                        # برای حفظ ساختار اصلی، فایل را در همان مسیر نسبی قرار می‌دهیم
                        rel_path = f"{dir_name}/{img_path.name}"
                        
                        # ایجاد آیتم تصویر
                        image = epub.EpubItem(
                            uid=f"{dir_name}_{img_path.stem}",
                            file_name=rel_path,
                            media_type=media_type,
                            content=image_content
                        )
                        
                        self.book.add_item(image)
                        image_count += 1
                        processed_images[img_path.name] = rel_path
                        
                        print(f"DEBUG: تصویر {img_path.name} به مسیر {rel_path} اضافه شد")
                    except Exception as e:
                        print(f"خطا در افزودن تصویر {img_path.name}: {e}")
            
            # پردازش زیرپوشه‌ها - به صورت بازگشتی
            for subdir in [d for d in dir_path.glob("*") if d.is_dir()]:
                subdir_name = subdir.name
                for ext in image_extensions:
                    for img_path in subdir.glob(f"**/*.{ext}"):
                        try:
                            with open(img_path, 'rb') as f:
                                image_content = f.read()
                            
                            # تعیین نوع رسانه
                            media_type = f"image/{ext}"
                            if ext == 'jpg':
                                media_type = "image/jpeg"
                            elif ext == 'svg':
                                media_type = "image/svg+xml"
                            
                            # محاسبه مسیر نسبی در داخل زیرپوشه
                            rel_in_subdir = img_path.relative_to(dir_path)
                            epub_path = f"{dir_name}/{rel_in_subdir}"
                            
                            # ایجاد آیتم تصویر
                            image = epub.EpubItem(
                                uid=f"{dir_name}_{subdir_name}_{img_path.stem}",
                                file_name=epub_path,
                                media_type=media_type,
                                content=image_content
                            )
                            
                            self.book.add_item(image)
                            image_count += 1
                            processed_images[str(rel_in_subdir)] = epub_path
                            
                            print(f"DEBUG: تصویر {rel_in_subdir} به مسیر {epub_path} اضافه شد")
                        except Exception as e:
                            print(f"خطا در افزودن تصویر {img_path}: {e}")
        
        # ذخیره اطلاعات تصاویر برای استفاده در تصحیح مسیرها
        self.processed_images = processed_images
        
        print(f"DEBUG: {image_count} تصویر به EPUB اضافه شد")
    
    def process_markdown_files(self, md_files, concatenate=False):
        """پردازش فایل‌های Markdown و تبدیل آن‌ها به فصل‌های EPUB
        
        Args:
            md_files (list): لیست مسیرهای فایل‌های Markdown
            concatenate (bool): آیا تمام فایل‌ها در یک فصل ترکیب شوند؟
        """
        if not md_files:
            print("خطا: هیچ فایل Markdown‌ای یافت نشد!")
            return
            
        print(f"DEBUG: پردازش {len(md_files)} فایل مارک‌داون...")
        print(f"DEBUG: آیا concatenate فعال است؟ {concatenate}")
        chapter_count = 0
        
        if concatenate:
            # ترکیب همه فایل‌ها در یک فصل
            chapter_title = self.metadata.title or self.main_dir.name
            chapter_content = ""
            
            for md_file in md_files:
                try:
                    content = self._read_file_with_different_encodings(md_file)
                    chapter_content += content + "\n\n"
                except Exception as e:
                    print(f"خطا در خواندن فایل {md_file}: {e}")
            
            # ایجاد یک فصل واحد
            self._create_chapter(chapter_title, chapter_content, "chapter_all")
            chapter_count += 1
            
        else:
            # استخراج اطلاعات متادیتا
            metadata_chapters = {}
            if self.metadata and hasattr(self.metadata, 'chapters'):
                for chapter in self.metadata.chapters:
                    if 'md_file' in chapter:
                        metadata_chapters[chapter['md_file']] = chapter

            print(f"DEBUG: تعداد فصل‌ها در متادیتا: {len(metadata_chapters)}")
            
            # گروه‌بندی فایل‌ها بر اساس فایل HTML (فصل) در متادیتا
            chapters_by_html = {}
            
            for md_file in md_files:
                try:
                    md_filename = Path(md_file).name
                    
                    # بررسی وجود اطلاعات فصل در متادیتا
                    chapter_info = metadata_chapters.get(md_filename, {})
                    
                    # اگر اطلاعات فصل پیدا نشد، این فایل را به عنوان یک فصل جداگانه اضافه می‌کنیم
                    if not chapter_info or 'html_file' not in chapter_info:
                        print(f"WARNING: فایل {md_filename} در متادیتا یافت نشد. به عنوان فصل جداگانه اضافه می‌شود.")
                        html_file = f"unknown_{md_filename}"
                        order = len(chapters_by_html) + 1
                    else:
                        html_file = chapter_info['html_file']
                        order = chapter_info.get('order', 0)
                    
                    # اضافه کردن به گروه مربوطه
                    if html_file not in chapters_by_html:
                        chapters_by_html[html_file] = {
                            'files': [],
                            'title': None,
                            'order': order
                        }
                    
                    # خواندن محتوای فایل
                    content = self._read_file_with_different_encodings(md_file)
                    
                    # استخراج عنوان از متادیتا یا محتوا
                    title = None
                    if 'title' in chapter_info:
                        title = chapter_info['title']
                    else:
                        title = self._extract_title_from_markdown(content)
                    
                    # اضافه کردن فایل به گروه با اطلاعات ترتیب
                    chapters_by_html[html_file]['files'].append({
                        'content': content,
                        'order': order,
                        'md_file': md_filename,
                        'title': title
                    })
                    
                    # استفاده از اولین عنوان معتبر به عنوان عنوان فصل
                    if title and not chapters_by_html[html_file]['title']:
                        chapters_by_html[html_file]['title'] = title
                    
                except Exception as e:
                    print(f"خطا در پردازش فایل {md_file}: {e}")
            
            # اکنون فایل‌ها را براساس html_file گروه‌بندی کرده‌ایم. برای هر گروه یک فصل ایجاد می‌کنیم
            print(f"DEBUG: {len(chapters_by_html)} فصل HTML یافت شد.")
            
            for html_file, chapter_data in chapters_by_html.items():
                try:
                    if not chapter_data['files']:
                        continue
                        
                    # مرتب‌سازی فایل‌ها براساس ترتیب
                    sorted_files = sorted(chapter_data['files'], key=lambda x: x['order'])
                    
                    # ایجاد عنوان فصل
                    chapter_title = chapter_data['title'] or f"فصل {html_file}"
                    
                    # ترکیب محتوای فایل‌ها
                    chapter_content = ""
                    for file_info in sorted_files:
                        chapter_content += file_info['content'] + "\n\n"
                    
                    print(f"DEBUG: ایجاد فصل '{chapter_title}' از {len(sorted_files)} فایل مارک‌داون")
                    
                    # استفاده از نام کامل فایل HTML به عنوان شناسه فصل
                    chapter_id = html_file
                    
                    print(f"DEBUG: استفاده از فایل HTML اصلی '{html_file}' به عنوان شناسه فصل")
                    
                    self._create_chapter(chapter_title, chapter_content, chapter_id)
                    chapter_count += 1
                    
                except Exception as e:
                    print(f"خطا در ایجاد فصل {html_file}: {e}")
            
            print(f"DEBUG: تعداد کل فصل‌های ایجاد شده: {chapter_count}")
    
    def _read_file_with_different_encodings(self, file_path):
        """خواندن فایل با کدگذاری‌های مختلف
        
        Args:
            file_path (str): مسیر فایل
            
        Returns:
            str: محتوای فایل
        """
        encodings = ['utf-8', 'utf-8-sig', 'cp1256', 'windows-1256', 'ISO-8859-6', 'arabic']
        success = False
        content = ""
        
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    content = f.read()
                    # print(f"DEBUG: فایل {Path(file_path).name} با کدگذاری {encoding} خوانده شد.")
                    success = True
                    break
            except UnicodeDecodeError:
                continue
        
        if not success:
            print(f"WARNING: خواندن فایل {file_path} با هیچ کدگذاری‌ای موفق نبود! تلاش مجدد با بایت‌های خام...")
            # تلاش آخر: خواندن به صورت بایت و تبدیل به utf-8
            with open(file_path, 'rb') as f:
                raw_bytes = f.read()
                content = raw_bytes.decode('utf-8', errors='replace')
        
        # بررسی محتوای مارک‌داون
        if not content or content.strip() == "":
            print(f"WARNING: محتوای فایل {Path(file_path).name} خالی است!")
            
        return content
    
    def _extract_title_from_markdown(self, content):
        """استخراج عنوان از محتوای Markdown
        
        Args:
            content (str): محتوای Markdown
            
        Returns:
            str: عنوان استخراج شده یا None
        """
        # بررسی خط اول برای یافتن عنوان با فرمت #
        lines = content.strip().split('\n')
        if lines and lines[0].strip().startswith('#'):
            title_line = lines[0].strip()
            # حذف نشانه‌های # از ابتدای خط
            title = re.sub(r'^#+\s*', '', title_line)
            return title.strip()
        
        return None
    
    def _create_chapter(self, title, content, chapter_id):
        """ایجاد یک فصل EPUB از محتوای Markdown
        
        Args:
            title (str): عنوان فصل
            content (str): محتوای Markdown
            chapter_id (str): شناسه یکتا برای فصل
        """
        # بررسی محتوای مارک‌داون
        if not content or content.strip() == "":
            print(f"WARNING: محتوای مارک‌داون برای فصل '{title}' خالی است!")
            content = f"# {title}\n\nبدون محتوا"
            
        # اطمینان از وجود عنوان در ابتدای محتوا
        if not content.strip().startswith('#'):
            content = f"# {title}\n\n{content}"
            
        # تبدیل Markdown به HTML
        html_content = markdown.markdown(content, extensions=['tables', 'fenced_code'])
        
        # بررسی محتوای HTML
        if not html_content or html_content.strip() == "":
            print(f"WARNING: محتوای HTML برای فصل '{title}' خالی است!")
            html_content = f"<h1>{title}</h1><p>بدون محتوا</p>"
        
        # تصحیح مسیرهای تصاویر
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # اصلاح تگ‌های تصویر
        for img in soup.find_all('img'):
            if img.get('src'):
                src_path = img['src']
                original_src = src_path
                
                # حالت‌های مختلف مسیرهای تصاویر
                # 1. assets/image.jpg - مسیر ساده
                # 2. graphics/image.jpg - مسیر با پوشه متفاوت
                # 3. graphics/subdir/image.jpg - مسیر با زیرپوشه
                # 4. ../images/image.jpg - مسیر نسبی به بالا
                # 5. /images/image.jpg - مسیر از ریشه
                
                # بررسی اینکه آیا مسیر دقیقاً همینطور در EPUB وجود دارد
                if hasattr(self, 'processed_images'):
                    # اگر مسیر کامل در processed_images وجود دارد
                    if src_path in self.processed_images:
                        img['src'] = self.processed_images[src_path]
                        print(f"DEBUG: تصویر '{original_src}' به '{img['src']}' تبدیل شد (تطبیق دقیق)")
                        continue
                    
                    # استخراج نام فایل از مسیر
                    filename = Path(src_path).name
                    
                    # جستجو بر اساس نام فایل
                    if filename in self.processed_images:
                        img['src'] = self.processed_images[filename]
                        print(f"DEBUG: تصویر '{original_src}' به '{img['src']}' تبدیل شد (تطبیق نام فایل)")
                        continue
                    
                    # جستجو در مسیرهای احتمالی
                    possible_path_key = None
                    for key in self.processed_images:
                        if key.endswith(src_path) or src_path.endswith(key):
                            possible_path_key = key
                            break
                            
                    if possible_path_key:
                        img['src'] = self.processed_images[possible_path_key]
                        print(f"DEBUG: تصویر '{original_src}' به '{img['src']}' تبدیل شد (تطبیق قسمتی)")
                        continue
                
                # استخراج پوشه و نام فایل
                try:
                    path_parts = Path(src_path)
                    base_dir = path_parts.parts[0] if len(path_parts.parts) > 1 else None
                    filename = path_parts.name
                except:
                    base_dir = None
                    filename = src_path.split('/')[-1] if '/' in src_path else src_path
                
                # اگر مسیر با assets/ شروع می‌شود و processed_images ندارد، آن را حفظ کنیم
                if src_path.startswith('assets/'):
                    # مسیر را همانطور حفظ می‌کنیم
                    pass
                # اگر مسیر با graphics/ شروع می‌شود، آن را حفظ کنیم
                elif src_path.startswith('graphics/'):
                    # مسیر را همانطور حفظ می‌کنیم
                    pass
                # اگر مسیر با ../images/ یا /images/ شروع می‌شود، فقط نام فایل را استخراج کنیم
                elif '../images/' in src_path or '/images/' in src_path:
                    img_name = src_path.split('/')[-1]
                    img['src'] = f'images/{img_name}'
                # اگر مسیر با images/ شروع نمی‌شود، به مسیر images/ اضافه کنیم
                elif 'images/' not in src_path and not src_path.startswith(('assets/', 'graphics/')):
                    img['src'] = f'images/{src_path}'
                
                print(f"DEBUG: تصویر '{original_src}' به '{img['src']}' تبدیل شد")
        
        # ایجاد فصل EPUB
        print(f"DEBUG: ایجاد فایل '{chapter_id}' برای فصل '{title}'")
        
        chapter = epub.EpubHtml(
            title=title,
            file_name=chapter_id,
            lang=self.language
        )
        
        # افزودن استایل به فصل
        chapter.add_item(self.book.get_item_with_id('style_default'))
        
        # تنظیم محتوای فصل
        chapter.content = str(soup)
        
        # افزودن فصل به کتاب
        self.book.add_item(chapter)
        self.chapters.append(chapter)
        
        # افزودن به فهرست مطالب
        self.toc.append(epub.Link(chapter_id, title, chapter_id))
    
    def finalize_book(self):
        """نهایی‌سازی کتاب EPUB و ذخیره آن"""
        if not self.chapters:
            print("خطا: هیچ فصلی برای کتاب ایجاد نشده است!")
            return False
        
        # ایجاد فهرست مطالب
        self.book.toc = self.toc
        
        # ایجاد اسپاین - ترتیب نمایش فصل‌ها
        self.book.spine = ['nav'] + self.chapters
        
        # افزودن فهرست مطالب خودکار
        self.book.add_item(epub.EpubNcx())
        self.book.add_item(epub.EpubNav())
        
        # ذخیره کتاب
        try:
            epub.write_epub(self.output_file, self.book, {})
            print(f"کتاب EPUB با موفقیت در {self.output_file} ذخیره شد.")
            return True
        except Exception as e:
            print(f"خطا در ذخیره کتاب EPUB: {e}")
            return False
    
    def add_font(self):
        """افزودن فونت فارسی به EPUB"""
        try:
            print("DEBUG: شروع افزودن فونت‌های فارسی Zar...")
            
            # تعریف فونت‌ها برای افزودن
            fonts = [
                {"name": "BZar.ttf", "uid": "font_zar", "desc": "معمولی"},
                {"name": "BZar-Bold.ttf", "uid": "font_zar_bold", "desc": "ضخیم"}
            ]
            
            for font in fonts:
                # تلاش برای یافتن فونت در مسیرهای مختلف
                font_paths = [
                    # مسیر نسبی از پوشه کتاب (main_dir)
                    Path(self.main_dir) / "assets" / "fonts" / "zar" / font["name"],
                    
                    # مسیر نسبی از پوشه اصلی پروژه
                    Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) / "assets" / "fonts" / "zar" / font["name"],
                    
                    # مسیر مطلق
                    Path(f"/home/basalam3785/Projects/Revenue/books/engine/assets/fonts/zar/{font['name']}")
                ]
                
                font_path = None
                for path in font_paths:
                    if path.exists():
                        font_path = path
                        print(f"DEBUG: فونت {font['desc']} در مسیر {font_path} یافت شد")
                        break
                
                if not font_path:
                    print(f"WARNING: فایل فونت {font['name']} در هیچ مسیری یافت نشد!")
                    print(f"DEBUG: مسیرهای جستجو شده: {', '.join(str(p) for p in font_paths)}")
                    continue
                
                print(f"DEBUG: افزودن فونت فارسی {font['desc']} از مسیر: {font_path}")
                
                # خواندن محتوای فایل فونت
                with open(font_path, 'rb') as f:
                    font_content = f.read()
                
                # افزودن فونت به EPUB
                font_item = epub.EpubItem(
                    uid=font["uid"],
                    file_name=f"fonts/{font['name']}",
                    media_type="application/x-font-truetype",
                    content=font_content
                )
                
                self.book.add_item(font_item)
                print(f"DEBUG: فونت فارسی {font['desc']} با موفقیت به EPUB اضافه شد")
            
        except Exception as e:
            print(f"ERROR: خطا هنگام افزودن فونت‌ها: {e}") 
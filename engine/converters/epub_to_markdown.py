#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path

# اضافه کردن مسیر پروژه به PYTHONPATH
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from utils.text_splitter import TextSplitter
from utils.file_manager import FileManager
from models.metadata import Metadata, MetadataManager
from converters.epub_parser import EpubParser

class EpubToMarkdownConverter:
    """کلاس مسئول تبدیل EPUB به فایل‌های Markdown"""
    
    def __init__(self, epub_path, min_words=150, file_manager:FileManager=None):
        """
        راه‌اندازی تبدیل‌کننده EPUB به Markdown
        
        Args:
            epub_path (str): مسیر فایل EPUB
            min_words (int): حداقل تعداد کلمات در هر فایل Markdown
            file_manager (FileManager): نمونه FileManager سینگلتون
        """
        self.epub_path = Path(epub_path)
        self.min_words = min_words
        
        # دریافت نام کتاب از نام فایل EPUB
        if self.epub_path.exists():
            self.book_name = self.epub_path.stem
        else:
            raise FileNotFoundError(f"فایل EPUB یافت نشد: {epub_path}")
        
        # استفاده از FileManager سینگلتون که از بیرون ارسال شده است
        self.base_dir = self.epub_path.parent
        
        self.file_manager = file_manager
        
        # دریافت مسیرهای کتاب از FileManager
        self.paths = self.file_manager.get_book_paths(self.book_name)
        self.dirs = self.paths  # برای سازگاری با کد قبلی
        
        # اطمینان از وجود پوشه‌های مورد نیاز
        for dir_name in ["book_dir", "images_dir", "en_dir", "fa_dir"]:
            self.file_manager.ensure_dir_exists(self.paths[dir_name])
        
        # ایجاد سایر اشیاء مورد نیاز
        self.metadata_manager = MetadataManager(self.paths["book_dir"], file_manager=self.file_manager)
        self.text_splitter = TextSplitter(min_words=min_words)
        self.epub_parser = EpubParser(epub_path)
    
    def convert(self):
        """
        تبدیل EPUB به فایل‌های Markdown
        
        Returns:
            bool: True در صورت موفقیت، False در صورت شکست
        """
        print(f"در حال تبدیل {self.epub_path}...")
        
        # بارگیری و تجزیه فایل EPUB
        if not self.epub_parser.load():
            return False
        
        # ایجاد متادیتا
        metadata = Metadata(
            title=self.epub_parser.metadata.get('title'),
            creator=self.epub_parser.metadata.get('creator'),
            language=self.epub_parser.metadata.get('language'),
            original_file=str(self.epub_path),
            direction=self.epub_parser.metadata.get('direction')
        )
        
        # استخراج تصاویر
        self._extract_images()
        
        # پردازش فصل‌ها
        chapter_count = self._process_chapters(metadata)
        
        # ذخیره متادیتا
        self.metadata_manager.save_metadata(metadata)
        
        # ایجاد فایل prompt.md
        md_files_count = self.file_manager.count_files('en/*.md', book_name=self.book_name)
        # استفاده از مسیر مناسب از get_book_paths
        prompt_file_path = self.paths["book_dir"] / "prompt.md"
        
        # استفاده از مسیرهای صحیح از FileManager
        en_dir = self.paths["en_dir"]
        fa_dir = self.paths["fa_dir"]
        
        # استخراج مسیرهای نسبی پوشه‌ها
        en_path = str(en_dir.relative_to(self.file_manager.base_dir))
        fa_path = str(fa_dir.relative_to(self.file_manager.base_dir))
        
        text = f"""
شما یک سیستم هوش مصنوعی پیشرفته در زمینه ویراستاری زبان فارسی هستید. هدف شما، ارائه متونی رسا، زیبا و مطابق با استانداردهای زبان فارسی است.
        

میخواهم تمامی فایل های درون {en_path} را به فارسی ترجمه کنم و در پوشه {fa_path} بریزم

نحوه اجرا:

دقت داشته باش که {md_files_count} فایل درون پوشه {en_path} است
فایل ها *.md هستند
تمام انها را به ترتیب از  part قبلی که ترجمه کردی تا part{md_files_count} ترجمه کن
در هنگام ترجمه فرمت markdown را حفظ کن و همه موارد را انتقال بده
این کار رو بدون نوشتن اسکریپت انجام بده و فقط md تولید کن
سوالی نپرس و فقط md تولید کن
برای خواندن فایل ها از cat استفاده کن

نحو ترجمه:

شما یک سیستم هوش مصنوعی پیشرفته در زمینه ویراستاری زبان فارسی هستید. هدف شما، ارائه متونی رسا، زیبا و مطابق با استانداردهای زبان فارسی است. با توجه به آموزش «ویراستاری و مهارت‌های درست‌نویسی» و تخصص خود در مهندسی هوش مصنوعی، وظایف خود را با درک عمیق مفاهیم زیر انجام دهید:


«شما یک مترجم و ویراستار حرفه‌ای هستید که در حوزه مهندسی نرم‌افزار و فناوری اطلاعات تخصص دارید. لطفاً متن زیر را از زبان انگلیسی به زبان فارسی ویراستاری و ترجمه کنید.


در انجام این کار، موارد زیر را رعایت کنید:


اطمینان حاصل کنید که تمام مفاهیم فنی و تخصصی مهندسی نرم‌افزار را به‌طور صحیح و کامل منتقل می‌کنید.
در صورت وجود اصطلاحات یا عبارات تخصصی، معادل‌های رایج و صحیح در فارسی را به کار ببرید یا در صورت نیاز، توضیح مختصری ارائه دهید.
هر انچه نیاز از به عنوان لغت در زبان اصلی در پاورقی ذکر شود در پرانتز بیاورید.
اگر متن اصلی سبک رسمی یا نیمه‌رسمی دارد، در ترجمه نیز همین سطح رسمیت را حفظ کنید.
در صورت وجود کد، مثال یا شبه‌کد (pseudo-code)، آن را به همان شکل نگه دارید .
مراقب باشید هیچ بخشی از متن را حذف نکنید یا به متن اصلی اطلاعات اضافی اضافه نکنید؛ تنها در صورت نیاز (مثلاً برای معادل‌های تخصصی نامأنوس) توضیح خیلی مختصر در پرانتز یا پانویس بیاورید.
در صورت وجود واژگان فارسی مصوب یا جاافتاده در حوزه مهندسی نرم‌افزار (مانند «سامانه» به‌جای «سیستم»، «پودمان» به‌جای «ماژول» و...) از آن‌ها استفاده کنید؛ اما اگر کاربرد واژه انگلیسی رواج بیشتری دارد، به شکل ترجمه‌شده یا با توضیح کوتاه به کار ببرید.
در تمام موارد برای لغات تخصصی ، معادل انگلیسی آن را در پارانتز جلوی آن قرار بده (مانند پاورقی در کتاب ها)

به عنوان یک ویراستار، نه تنها غلط‌یاب، بلکه تسهیل‌گر انتقال معنا، ایجادکننده تعامل، احیاگر متن و پاسدار زبان فارسی باشید.

از رویکردی فعال و خلاقانه برای بهبود کیفیت زبانی متن استفاده کنید و از تغییرات صرفاً مکانیکی پرهیز کنید.

ویراستاری به معنای پیراستن متن از خطاها، ابهامات و نارسايي‌ها، و رساندن آن به بالاترین سطح کیفیت زبانی است و تو باید این کار را انجام بدی.

ویراستاری شامل مراحل مختلفی است، که باید تمام آن ها را در متنی که برایم تولید می کنی رعایت کنی.
۱-بررسی املایی و نشانه‌گذاری و ویراستاری صوری
۲-اصلاح ساختار جملات و عبارات
۳-ویرایش محتوایی (اطمینان از صحت اطلاعات و انسجام منطقی متن)
۴-ویرایش زبانی (بهبود لحن و سبک نگارش)


ویراستاری صوری (ظاهری):

نشانه‌گذاری: بررسی و اصلاح نشانه‌گذاری با هدف بهبود خوانایی، وضوح معنا و انتقال لحن.

انواع نشانه‌ها: نقطه (.), کاما (,)، نقطه‌کاما (;)، دونقطه (:), سه‌نقطه (...), علامت پرسش (؟), علامت عاطفی (!), گیومه («») پرانتز (()), کروشه ([]).

نکات کلیدی:

کاما: جداسازی اجزای جمله، جداسازی فهرست‌ها، نشان دادن مکث کوتاه

نقطه: پایان جمله، نشان دادن اختصار

نقطه‌کاما: ایجاد تعادل بین نقطه و کاما، ایجاد ارتباط بین جملات مرتبط

سه‌نقطه: حذف بخشی از متن، نشان دادن مکث طولانی، ایجاد تعلیق

گیومه: نقل قول مستقیم، تأکید بر یک واژه، نام‌گذاری

پرانتز: توضیحات اضافی، ارجاعات درون‌متنی، معادل‌های واژه‌ها

کروشه: افزودن توضیحات توسط ویراستار، نشان دادن حذف بخشی از متن اصلی


ویراستاری زبانی:

انتخاب واژگان: انتخاب واژگان مناسب، گویا و رسا برای انتقال دقیق منظور نویسنده و از معادل‌های فارسی رایج و معیار استفاده کنید.

مثال: به جای «ایفاد» از «انجام دادن» استفاده کنید، و به جای اصطلاحات عامیانه مانند "اِکی" از معادل های رسمی استفاده کنید.

گرته‌برداری: اجتناب از گرته‌برداری‌های نامناسب و نامأنوس که باعث کاهش کیفیت زبانی متن می‌شوند.

راهنما: از واژه‌های دخیل مناسب یا گرته‌برداری‌های ترکیبی (با رعایت اصول زبان فارسی) استفاده کنید.

مثال: به جای «تحت‌اللفظی» از «لفظ به لفظ» استفاده کنید.

کژتابی (ابهام): رفع ابهام از جملات و عبارات با هدف جلوگیری از برداشت‌های نادرست.

علل کژتابی: نامشخص بودن مرجع ضمیر، ساختارهای پیچیده، فشرده‌گویی بیش از حد، حذف اجزای ضروری جمله.

مثال: "من مثل شما بلد نیستم" (آیا نویسنده "مهارت" شخص مقابل را ندارد یا "اعتقاد" او را؟)

حشونویسی و درازنویسی: حذف تکرارهای غیرضروری و کوتاه کردن جملات برای افزایش تمرکز و خوانایی متن.

راهنما: از تکرار بی‌مورد واژه‌ها و عبارات و طولانی کردن بی‌دلیل جملات خودداری کنید.

مثال: "این موضوع بسیار بسیار مهم است" (بهتر است: "این موضوع بسیار مهم است").

کاربرد نادرست فعل: استفاده از فعل‌های نامناسب، ناهمخوان با نهاد، یا به شکل غیرفصیح.

راهنما: به هماهنگی فعل و نهاد، وجه فعل، و انتخاب فعل مناسب با توجه به زمان و معنای جمله دقت کنید.

مثال: "رزمندگان به دشمن یورش برد" (بهتر است: "رزمندگان به دشمن یورش بردند").

کاربرد نادرست حرف: استفاده از حروف اضافه و ربط به شکل نادرست یا غیرفصیح.

راهنما: به کاربرد صحیح حروف و نقش آنها در جمله توجه کنید.

مثال: "او علاقه‌مند به ادبیات است" (بهتر است: "او علاقه‌مند ادبیات است").

خطاهای آوایی: اجتناب از صداهای ناخوشایند در متن به دلیل تکرار، تتابع اضافات، و تنافر حروف و کلمات.

راهنما: به آهنگ و روانی زبان در هنگام خواندن متن توجه کنید.

مثال: "کتابی خوب و خوب و خوب" (بهتر است: "کتابی بسیار خوب").

معیارنویسی انجام بده! یعنی استفاده از زبانی که در عین زیبایی و رسایی، منطبق بر قواعد زبان فارسی و قابل فهم برای عموم باشد.



خروجی:

ویژگی‌های متن خروجی باید بر اساس قواعد زیر در زبان معیار باشد:

۱-منطبق بودن بر دستور زبان فارسی
۲-انتقال بیشترین مفاهیم با کمترین واژه‌ها
۳-استفاده از واژه‌های رایج و قابل فهم
۴-نزدیک بودن به زبان گفتار (در عین پرهیز از عامیانه‌نویسی)
۵-شفافیت، رسایی و منطقی بودن
۶-پرهیز از بار احساسی و جانبداری

سایر ویژگی های مهم متن خروجی:
متن نهایی باید رسا، زیبا، روان و مطابق با استانداردهای زبان فارسی باشد.
متن نهایی باید به صورت markdown باشد و متن ورودی هم markdown است و المان های درون مارک‌دان نباید از بین بروند
متن نهایی باید فارسی و با زبان معیار باشد.
متن نهایی باید ویرستاری ادبی شده باشد.
در جاهایی که لازم است برای خوانایی بهتر از کسره استفاده کن اما زیاده روی استفاده از کسره منجر به تتابع اضافات و پیچیدگی میشه و فقط زمانی که مجبور هستی از کسره استفاده کن
متن نهایی نباید گرته برداری از انگلیسی داشته باشد
متن نهایی نباید درازه گویی داشته باشد.
متن نهایی نباید ویراستاری صوری شده باشد.
متن نهایی نباید کژتابی داشته باشد.
متن نهایی نباید تتابع افعال ، جدا افتادگی اجزای فعل ، تتابع اضافات و... داشته باشد.
جملات متن نهایی باید خوانا و بدون پیچیدگی باشد.



شروع کار:
ترجمه را آغاز کن و 
توقف نکن و تا فایل {md_files_count} ادامه بده
        """
        with open(prompt_file_path, 'w', encoding='utf-8') as f:
            f.write(text)
        
        print(f"فایل prompt.md ایجاد شد: {prompt_file_path}")
        print(f"تبدیل کتاب {self.epub_path.name} با موفقیت انجام شد.")
        print(f"تعداد فصل‌ها: {chapter_count}")
        print(f"تعداد فایل‌های Markdown انگلیسی: {md_files_count}")
        print(f"تعداد تصاویر: {len(self.epub_parser.images)}")
        print(f"فایل metadata.json در {self.paths['book_dir'] / 'metadata.json'} ذخیره شد.")
        
        return True
    
    def _extract_images(self):
        """استخراج و ذخیره تصاویر از EPUB"""
        for image in self.epub_parser.images:
            try:
                image_name = image['file_name'].split('/')[-1]
                self.file_manager.save_image(image['content'], image_name, book_name=self.book_name)
            except Exception as e:
                print(f"خطا در استخراج تصویر {image['file_name']}: {e}")
    
    def _process_chapters(self, metadata):
        """پردازش فصل‌های EPUB و تبدیل به Markdown
        
        Args:
            metadata (Metadata): آبجکت متادیتا برای ذخیره اطلاعات فصل‌ها
            
        Returns:
            int: تعداد فصل‌های پردازش شده
        """
        chapter_count = 0
        chunk_num = 1
        
        print(f"تعداد کل فصل‌ها برای پردازش: {len(self.epub_parser.chapters)}")
        
        for i, chapter in enumerate(self.epub_parser.chapters):
            try:
                # استفاده از عنوان استخراج شده توسط epub_parser
                chapter_title = chapter['title'] if chapter.get('title') else f"فصل {i+1}"
                print(f"در حال پردازش فصل {i+1}/{len(self.epub_parser.chapters)}: {chapter_title}")
                
                # تبدیل HTML به Markdown
                markdown_content = self.epub_parser.convert_html_to_markdown(chapter['html_content'])
                
                # تقسیم متن به قطعات کوچکتر
                chunks = self.text_splitter.split_text(markdown_content)
                print(f"فصل به {len(chunks)} قطعه تقسیم شد")
                
                # ذخیره هر قطعه در یک فایل Markdown جداگانه
                for j, chunk in enumerate(chunks):
                    md_filename = f"part{chunk_num}.md"
                    # print(f"  ایجاد فایل {md_filename} برای قطعه {j+1} از فصل {i+1}")
                    
                    # ایجاد عنوان مناسب برای هر قطعه
                    # فقط برای قطعات بیشتر از یکی، شماره قطعه را اضافه می‌کنیم
                    chunk_title = chapter_title
                    if len(chunks) > 1:
                        chunk_title = f"{chapter_title} - قسمت {j+1}/{len(chunks)}"
                    
                    # اضافه کردن اطلاعات قطعه به متادیتا
                    metadata.add_chapter(
                        md_file=md_filename,
                        title=chunk_title,
                        html_file=chapter['file_name'],
                        order=chunk_num  # ترتیب براساس شماره قطعه
                    )
                    
                    # اضافه کردن عنوان فصل به اولین بخش
                    if j == 0 and chapter_title:
                        chunk = f"# {chapter_title}\n\n{chunk}"
                    
                    self.file_manager.write_markdown_file(chunk, md_filename, 'en', book_name=self.book_name)
                    chunk_num += 1
                
                chapter_count += 1
                
            except Exception as e:
                print(f"خطا در پردازش فصل {i+1} ({chapter.get('title', f'فصل {i+1}')}): {e}")
                
        print(f"تعداد کل فایل‌های Markdown ایجاد شده: {chunk_num-1}")
        print(f"تعداد فصل‌های پردازش شده: {chapter_count}")
        return chapter_count 
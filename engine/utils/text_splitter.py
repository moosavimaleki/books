#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nltk
from nltk.tokenize import sent_tokenize

# اطمینان از دانلود داده‌های مورد نیاز NLTK
try:
    nltk.download('punkt', quiet=True)
except:
    pass

class TextSplitter:
    """کلاس مسئول تقسیم متن به قطعات کوچکتر براساس قوانین خاص"""
    
    def __init__(self, min_words=150, max_words=300, overflow_limit=400):
        """
        راه‌اندازی TextSplitter با پارامترهای قابل تنظیم
        
        Args:
            min_words (int): حداقل تعداد کلمات در هر قطعه
            max_words (int): حداکثر تعداد کلمات در هر قطعه در حالت ایده‌آل
            overflow_limit (int): حد بالایی تعداد کلمات که پس از آن پاراگراف باید تقسیم شود
        """
        self.min_words = min_words
        self.max_words = max_words
        self.overflow_limit = overflow_limit
    
    def count_words(self, text):
        """شمارش تعداد کلمات در یک متن
        
        Args:
            text (str): متن برای شمارش کلمات
            
        Returns:
            int: تعداد کلمات در متن
        """
        if not text:
            return 0
        return len(text.split())
    
    def split_paragraph(self, paragraph):
        """تقسیم یک پاراگراف به قطعات کوچکتر براساس قوانین تعیین شده
        
        قوانین:
        1. اگر یک پاراگراف 300 کلمه یا کمتر دارد، آن را به عنوان یک قطعه نگه دار.
        2. اگر یک پاراگراف بین 301 تا 400 کلمه دارد، همچنان آن را به عنوان یک قطعه نگه دار.
        3. اگر یک پاراگراف بیش از 400 کلمه دارد، آن را در مرزهای جمله تقسیم کن.
        4. استثنا: اگر یک جمله تنها بیش از 400 کلمه دارد، کل آن را در یک قطعه نگه دار.
        
        Args:
            paragraph (str): پاراگراف برای تقسیم
            
        Returns:
            list: لیستی از قطعات متنی
        """
        word_count = self.count_words(paragraph)
        
        # قانون 1 و 2: پاراگراف‌های کوچک را تقسیم نکن
        if word_count <= self.overflow_limit:
            return [paragraph]
        
        # قانون 3: تقسیم پاراگراف‌های بزرگ در مرزهای جمله
        sentences = sent_tokenize(paragraph)
        chunks = []
        current_chunk = []
        current_word_count = 0
        
        for sentence in sentences:
            sentence_word_count = self.count_words(sentence)
            
            # قانون 4: استثنا برای جملات بسیار طولانی
            if sentence_word_count > self.overflow_limit:
                # اگر قطعه فعلی خالی نیست، آن را به لیست قطعات اضافه کن
                if current_chunk:
                    chunks.append(" ".join(current_chunk))
                    current_chunk = []
                    current_word_count = 0
                
                # جمله طولانی را به عنوان یک قطعه مجزا اضافه کن
                chunks.append(sentence)
                continue
            
            # بررسی کن که آیا افزودن این جمله باعث تجاوز از حداکثر تعداد کلمات می‌شود
            if current_word_count + sentence_word_count > self.max_words:
                # قطعه فعلی را به لیست قطعات اضافه کن
                chunks.append(" ".join(current_chunk))
                current_chunk = [sentence]
                current_word_count = sentence_word_count
            else:
                # جمله را به قطعه فعلی اضافه کن
                current_chunk.append(sentence)
                current_word_count += sentence_word_count
        
        # باقیمانده جملات را به عنوان یک قطعه اضافه کن
        if current_chunk:
            chunks.append(" ".join(current_chunk))
        
        return chunks
    
    def merge_small_chunks(self, chunks):
        """ترکیب قطعات کوچک متن برای رسیدن به حداقل تعداد کلمات
        
        Args:
            chunks (list): لیستی از قطعات متنی
            
        Returns:
            list: لیستی از قطعات متنی ترکیب شده
        """
        if not chunks:
            return []
        
        merged_chunks = []
        current_chunk = chunks[0]
        current_word_count = self.count_words(current_chunk)
        
        for i in range(1, len(chunks)):
            next_chunk = chunks[i]
            next_word_count = self.count_words(next_chunk)
            
            # اگر قطعه فعلی کمتر از حداقل تعداد کلمات است و ترکیب آن با قطعه بعدی
            # از حداکثر تعداد کلمات تجاوز نمی‌کند، آن‌ها را ترکیب کن
            if current_word_count < self.min_words and current_word_count + next_word_count <= self.max_words:
                current_chunk += " " + next_chunk
                current_word_count += next_word_count
            else:
                # قطعه فعلی را به لیست قطعات ترکیب شده اضافه کن و به قطعه بعدی برو
                merged_chunks.append(current_chunk)
                current_chunk = next_chunk
                current_word_count = next_word_count
        
        # آخرین قطعه را اضافه کن
        merged_chunks.append(current_chunk)
        
        return merged_chunks
    
    def split_text(self, text):
        """تقسیم یک متن کامل به قطعات کوچکتر براساس پاراگراف‌ها و قوانین تعیین شده
        
        Args:
            text (str): متن کامل برای تقسیم
            
        Returns:
            list: لیستی از قطعات متنی تقسیم شده
        """
        # تقسیم متن به پاراگراف‌ها
        paragraphs = [p for p in text.split('\n\n') if p.strip()]
        
        # تقسیم هر پاراگراف براساس قوانین
        all_chunks = []
        for paragraph in paragraphs:
            paragraph_chunks = self.split_paragraph(paragraph)
            all_chunks.extend(paragraph_chunks)
        
        # ترکیب قطعات کوچک
        merged_chunks = self.merge_small_chunks(all_chunks)
        
        return merged_chunks 
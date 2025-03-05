# EPUB-Markdown Converter package initialization
"""
این پکیج شامل ابزارهای مختلف برای تبدیل فایل‌های EPUB به Markdown و برعکس است
"""

__version__ = "1.0.0"
__author__ = "basalam3785"

# ایجاد مسیر برای import ماژول‌ها
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# وارد کردن ماژول‌های اصلی
from utils import TextSplitter, FileManager
from models import Metadata, MetadataManager
from converters import (
    EpubParser, 
    EpubCreator, 
    EpubToMarkdownConverter, 
    MarkdownToEpubConverter
) 
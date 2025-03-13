#!/bin/bash

# Script to send a GitHub request every 16 minutes and log status every minute
# Created: March 13, 2025

# Function to send the curl request
send_request() {
  echo "$(date '+%Y-%m-%d %H:%M:%S') - Sending request to GitHub..."

  # Execute the curl command and capture the response
  response=$(curl -s 'https://github.com/moosavimaleki/books/pull/4/comment?sticky=true' \
    -H 'accept: application/json' \
    -H 'accept-language: en-US,en;q=0.9,fa;q=0.8' \
    -H 'cache-control: no-cache' \
    -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundaryBA75PYgSLXXBSt2w' \
    -H 'cookie: _octo=GH1.1.1668695001.1735100685; _device_id=1aea08ddf4f711e3f62280b086ac59ac; saved_user_sessions=1008267%3AxwIXvhN1HNTNENGXNsLiT-M-onh2tZ6HFcmFRw9W1r5XNsLu; user_session=xwIXvhN1HNTNENGXNsLiT-M-onh2tZ6HFcmFRw9W1r5XNsLu; __Host-user_session_same_site=xwIXvhN1HNTNENGXNsLiT-M-onh2tZ6HFcmFRw9W1r5XNsLu; logged_in=yes; dotcom_user=moosavimaleki; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; cpu_bucket=xlg; preferred_color_mode=dark; tz=Asia%2FTehran; _gh_sess=cn8NPuFjg0pLBsCUQIIRzfz9UckzqUFbdAgYRid0%2B7XRLCuAWyV1%2B2YP39%2FDSX3hn9nEnnJKYank6tZQbiLgyQeGXJTUQFQkSWruT%2BdT2cDKTcro4pUu2ShM1t21Bh8YQ2Vq2V2F3%2FReLEV07e2AyBPLZBKtv0Y0zanhOB1usIwzaXPgYhcQAYDcg4yW9Cua6%2FN08tgBVYtLPYqjpzMdFUbfGcwEKGzmKvMcnA%2BDgIKKSFHZr3Fs%2Bisef6jW%2BTOjnksEH1R6R94YgHVYaNIHFihAKqPXc4UAUWFg4rvB0Ccm0TppgEr9PJ2AWAMkB2LY65U44cOmPzWelwYrK3fT0V8fz%2B8GIn%2B8wre8AzMG1S6rbvfpy%2FgQVVmL6LUwq5jyfMP1vLUc%2FNBh7Yj4L3gkmmsRdVtAaHFcw4wTsVxO1qMbbTAk7E92QWh46fB0Z4pmSpok2TZP5L7qap86%2FhJNT3ticwluEbYajo96Xg%3D%3D--2OxndF2OEFEzd7dz--eJhQ%2B3th0wtQcCeleSCdKw%3D%3D' \
    -H 'origin: https://github.com' \
    -H 'pragma: no-cache' \
    -H 'priority: u=1, i' \
    -H 'referer: https://github.com/moosavimaleki/books/pull/4' \
    -H 'sec-ch-ua: "Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"' \
    -H 'sec-ch-ua-mobile: ?0' \
    -H 'sec-ch-ua-platform: "Linux"' \
    -H 'sec-fetch-dest: empty' \
    -H 'sec-fetch-mode: cors' \
    -H 'sec-fetch-site: same-origin' \
    -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' \
    -H 'x-requested-with: XMLHttpRequest' \
    -H 'x-timeline-last-modified: 2025-03-13T21:56:00.000000000+03:30' \
    --data-raw $'------WebKitFormBoundaryBA75PYgSLXXBSt2w\r\nContent-Disposition: form-data; name="authenticity_token"\r\n\r\nbXl23FdPY1CzXp07dz15PcPzJCtYFbm2repMgJUAdL9J-9DvnvpBolNAN4rFL6_83of0T_NjpP-UGWk_Sy6H6A\r\n------WebKitFormBoundaryBA75PYgSLXXBSt2w\r\nContent-Disposition: form-data; name="required_field_bdbb"\r\n\r\n\r\n------WebKitFormBoundaryBA75PYgSLXXBSt2w\r\nContent-Disposition: form-data; name="timestamp"\r\n\r\n1741891330456\r\n------WebKitFormBoundaryBA75PYgSLXXBSt2w\r\nContent-Disposition: form-data; name="timestamp_secret"\r\n\r\nb1cafa9a3d1804078891eb5d6d8e134edec8e88e0bee47e971b08cb86d1b7502\r\n------WebKitFormBoundaryBA75PYgSLXXBSt2w\r\nContent-Disposition: form-data; name="issue"\r\n\r\n4\r\n------WebKitFormBoundaryBA75PYgSLXXBSt2w\r\nContent-Disposition: form-data; name="saved_reply_id"\r\n\r\n\r\n------WebKitFormBoundaryBA75PYgSLXXBSt2w\r\nContent-Disposition: form-data; name="comment[body]"\r\n\r\nمیخواهم تمامی فایل های درون designing-data-intensive-applications/en را به فارسی ترجمه کنم و در پوشه designing-data-intensive-applications/fa بریزم\r\n\r\nدقت داشته باش که 1342 فایل درون پوشه designing-data-intensive-applications/en\r\n\r\nشما یک سیستم هوش مصنوعی پیشرفته در زمینه ویراستاری زبان فارسی هستید. هدف شما، ارائه متونی رسا، زیبا و مطابق با استانداردهای زبان فارسی است.\r\n\r\nمیخواهم تمامی فایل های درون {designing-data-intensive-applications/en} را به فارسی ترجمه کنم و در پوشه {designing-data-intensive-applications/fa} بریزم\r\n\r\nنحوه اجرا:\r\n\r\nدقت داشته باش که {1342} فایل درون پوشه {designing-data-intensive-applications/en} است\r\nفایل ها *.md هستند\r\nتمام انها را به ترتیب از part قبلی که ترجمه کردی تا part{md_files_count} ترجمه کن\r\nدر هنگام ترجمه فرمت markdown را حفظ کن و همه موارد را انتقال بده\r\nاین کار رو بدون نوشتن اسکریپت انجام بده و فقط md تولید کن\r\nسوالی نپرس و فقط md تولید کن\r\nبرای خواندن فایل ها از cat استفاده کن\r\n\r\nنحو ترجمه:\r\n\r\nشما یک سیستم هوش مصنوعی پیشرفته در زمینه ویراستاری زبان فارسی هستید. هدف شما، ارائه متونی رسا، زیبا و مطابق با استانداردهای زبان فارسی است. با توجه به آموزش «ویراستاری و مهارت‌های درست‌نویسی» و تخصص خود در مهندسی هوش مصنوعی، وظایف خود را با درک عمیق مفاهیم زیر انجام دهید:\r\n\r\n«شما یک مترجم و ویراستار حرفه‌ای هستید که در حوزه مهندسی نرم‌افزار و فناوری اطلاعات تخصص دارید. لطفاً متن زیر را از زبان انگلیسی به زبان فارسی ویراستاری و ترجمه کنید.\r\n\r\nدر انجام این کار، موارد زیر را رعایت کنید:\r\n\r\nاطمینان حاصل کنید که تمام مفاهیم فنی و تخصصی مهندسی نرم‌افزار را به‌طور صحیح و کامل منتقل می‌کنید.\r\nدر صورت وجود اصطلاحات یا عبارات تخصصی، معادل‌های رایج و صحیح در فارسی را به کار ببرید یا در صورت نیاز، توضیح مختصری ارائه دهید.\r\nهر انچه نیاز از به عنوان لغت در زبان اصلی در پاورقی ذکر شود در پرانتز بیاورید.\r\nاگر متن اصلی سبک رسمی یا نیمه‌رسمی دارد، در ترجمه نیز همین سطح رسمیت را حفظ کنید.\r\nدر صورت وجود کد، مثال یا شبه‌کد (pseudo-code)، آن را به همان شکل نگه دارید .\r\nمراقب باشید هیچ بخشی از متن را حذف نکنید یا به متن اصلی اطلاعات اضافی اضافه نکنید؛ تنها در صورت نیاز (مثلاً برای معادل‌های تخصصی نامأنوس) توضیح خیلی مختصر در پرانتز یا پانویس بیاورید.\r\nدر صورت وجود واژگان فارسی مصوب یا جاافتاده در حوزه مهندسی نرم‌افزار (مانند «سامانه» به‌جای «سیستم»، «پودمان» به‌جای «ماژول» و...) از آن‌ها استفاده کنید؛ اما اگر کاربرد واژه انگلیسی رواج بیشتری دارد، به شکل ترجمه‌شده یا با توضیح کوتاه به کار ببرید.\r\nدر تمام موارد برای لغات تخصصی ، معادل انگلیسی آن را در پارانتز جلوی آن قرار بده (مانند پاورقی در کتاب ها)\r\n\r\nبه عنوان یک ویراستار، نه تنها غلط‌یاب، بلکه تسهیل‌گر انتقال معنا، ایجادکننده تعامل، احیاگر متن و پاسدار زبان فارسی باشید.\r\n\r\nاز رویکردی فعال و خلاقانه برای بهبود کیفیت زبانی متن استفاده کنید و از تغییرات صرفاً مکانیکی پرهیز کنید.\r\n\r\nویراستاری به معنای پیراستن متن از خطاها، ابهامات و نارسايي‌ها، و رساندن آن به بالاترین سطح کیفیت زبانی است و تو باید این کار را انجام بدی.\r\n\r\nویراستاری شامل مراحل مختلفی است، که باید تمام آن ها را در متنی که برایم تولید می کنی رعایت کنی.\r\n۱-بررسی املایی و نشانه‌گذاری و ویراستاری صوری\r\n۲-اصلاح ساختار جملات و عبارات\r\n۳-ویرایش محتوایی (اطمینان از صحت اطلاعات و انسجام منطقی متن)\r\n۴-ویرایش زبانی (بهبود لحن و سبک نگارش)\r\n\r\nویراستاری صوری (ظاهری):\r\n\r\nنشانه‌گذاری: بررسی و اصلاح نشانه‌گذاری با هدف بهبود خوانایی، وضوح معنا و انتقال لحن.\r\n\r\nانواع نشانه‌ها: نقطه (.), کاما (,)، نقطه‌کاما (;)، دونقطه (:), سه‌نقطه (...), علامت پرسش (؟), علامت عاطفی (\u0021), گیومه («») پرانتز (()), کروشه ([]).\r\n\r\nنکات کلیدی:\r\n\r\nکاما: جداسازی اجزای جمله، جداسازی فهرست‌ها، نشان دادن مکث کوتاه\r\n\r\nنقطه: پایان جمله، نشان دادن اختصار\r\n\r\nنقطه‌کاما: ایجاد تعادل بین نقطه و کاما، ایجاد ارتباط بین جملات مرتبط\r\n\r\nسه‌نقطه: حذف بخشی از متن، نشان دادن مکث طولانی، ایجاد تعلیق\r\n\r\nگیومه: نقل قول مستقیم، تأکید بر یک واژه، نام‌گذاری\r\n\r\nپرانتز: توضیحات اضافی، ارجاعات درون‌متنی، معادل‌های واژه‌ها\r\n\r\nکروشه: افزودن توضیحات توسط ویراستار، نشان دادن حذف بخشی از متن اصلی\r\n\r\nویراستاری زبانی:\r\n\r\nانتخاب واژگان: انتخاب واژگان مناسب، گویا و رسا برای انتقال دقیق منظور نویسنده و از معادل‌های فارسی رایج و معیار استفاده کنید.\r\n\r\nمثال: به جای «ایفاد» از «انجام دادن» استفاده کنید، و به جای اصطلاحات عامیانه مانند "اِکی" از معادل های رسمی استفاده کنید.\r\n\r\nگرته‌برداری: اجتناب از گرته‌برداری‌های نامناسب و نامأنوس که باعث کاهش کیفیت زبانی متن می‌شوند.\r\n\r\nراهنما: از واژه‌های دخیل مناسب یا گرته‌برداری‌های ترکیبی (با رعایت اصول زبان فارسی) استفاده کنید.\r\n\r\nمثال: به جای «تحت‌اللفظی» از «لفظ به لفظ» استفاده کنید.\r\n\r\nکژتابی (ابهام): رفع ابهام از جملات و عبارات با هدف جلوگیری از برداشت‌های نادرست.\r\n\r\nعلل کژتابی: نامشخص بودن مرجع ضمیر، ساختارهای پیچیده، فشرده‌گویی بیش از حد، حذف اجزای ضروری جمله.\r\n\r\nمثال: "من مثل شما بلد نیستم" (آیا نویسنده "مهارت" شخص مقابل را ندارد یا "اعتقاد" او را؟)\r\n\r\nحشونویسی و درازنویسی: حذف تکرارهای غیرضروری و کوتاه کردن جملات برای افزایش تمرکز و خوانایی متن.\r\n\r\nراهنما: از تکرار بی‌مورد واژه‌ها و عبارات و طولانی کردن بی‌دلیل جملات خودداری کنید.\r\n\r\nمثال: "این موضوع بسیار بسیار مهم است" (بهتر است: "این موضوع بسیار مهم است").\r\n\r\nکاربرد نادرست فعل: استفاده از فعل‌های نامناسب، ناهمخوان با نهاد، یا به شکل غیرفصیح.\r\n\r\nراهنما: به هماهنگی فعل و نهاد، وجه فعل، و انتخاب فعل مناسب با توجه به زمان و معنای جمله دقت کنید.\r\n\r\nمثال: "رزمندگان به دشمن یورش برد" (بهتر است: "رزمندگان به دشمن یورش بردند").\r\n\r\nکاربرد نادرست حرف: استفاده از حروف اضافه و ربط به شکل نادرست یا غیرفصیح.\r\n\r\nراهنما: به کاربرد صحیح حروف و نقش آنها در جمله توجه کنید.\r\n\r\nمثال: "او علاقه‌مند به ادبیات است" (بهتر است: "او علاقه‌مند ادبیات است").\r\n\r\nخطاهای آوایی: اجتناب از صداهای ناخوشایند در متن به دلیل تکرار، تتابع اضافات، و تنافر حروف و کلمات.\r\n\r\nراهنما: به آهنگ و روانی زبان در هنگام خواندن متن توجه کنید.\r\n\r\nمثال: "کتابی خوب و خوب و خوب" (بهتر است: "کتابی بسیار خوب").\r\n\r\nمعیارنویسی انجام بده\u0021 یعنی استفاده از زبانی که در عین زیبایی و رسایی، منطبق بر قواعد زبان فارسی و قابل فهم برای عموم باشد.\r\n\r\nخروجی:\r\n\r\nویژگی‌های متن خروجی باید بر اساس قواعد زیر در زبان معیار باشد:\r\n\r\n۱-منطبق بودن بر دستور زبان فارسی\r\n۲-انتقال بیشترین مفاهیم با کمترین واژه‌ها\r\n۳-استفاده از واژه‌های رایج و قابل فهم\r\n۴-نزدیک بودن به زبان گفتار (در عین پرهیز از عامیانه‌نویسی)\r\n۵-شفافیت، رسایی و منطقی بودن\r\n۶-پرهیز از بار احساسی و جانبداری\r\n\r\nسایر ویژگی های مهم متن خروجی:\r\nمتن نهایی باید رسا، زیبا، روان و مطابق با استانداردهای زبان فارسی باشد.\r\nمتن نهایی باید به صورت markdown باشد و متن ورودی هم markdown است و المان های درون مارک‌دان نباید از بین بروند\r\nمتن نهایی باید فارسی و با زبان معیار باشد.\r\nمتن نهایی باید ویرستاری ادبی شده باشد.\r\nدر جاهایی که لازم است برای خوانایی بهتر از کسره استفاده کن اما زیاده روی استفاده از کسره منجر به تتابع اضافات و پیچیدگی میشه و فقط زمانی که مجبور هستی از کسره استفاده کن\r\nمتن نهایی نباید گرته برداری از انگلیسی داشته باشد\r\nمتن نهایی نباید درازه گویی داشته باشد.\r\nمتن نهایی **باید** ویراستاری صوری شده باشد. \r\nمتن نهایی نباید کژتابی داشته باشد.\r\nمتن نهایی نباید تتابع افعال ، جدا افتادگی اجزای فعل ، تتابع اضافات و... داشته باشد.\r\nجملات متن نهایی باید خوانا و بدون پیچیدگی باشد.\r\n\r\nشروع کار:\r\nترجمه را آغاز کن و\r\nتوقف نکن و تا فایل 1342 ادامه بده\r\n------WebKitFormBoundaryBA75PYgSLXXBSt2w\r\nContent-Disposition: form-data; name="path"\r\n\r\n\r\n------WebKitFormBoundaryBA75PYgSLXXBSt2w\r\nContent-Disposition: form-data; name="line"\r\n\r\n\r\n------WebKitFormBoundaryBA75PYgSLXXBSt2w\r\nContent-Disposition: form-data; name="start_line"\r\n\r\n\r\n------WebKitFormBoundaryBA75PYgSLXXBSt2w\r\nContent-Disposition: form-data; name="preview_side"\r\n\r\n\r\n------WebKitFormBoundaryBA75PYgSLXXBSt2w\r\nContent-Disposition: form-data; name="preview_start_side"\r\n\r\n\r\n------WebKitFormBoundaryBA75PYgSLXXBSt2w\r\nContent-Disposition: form-data; name="start_commit_oid"\r\n\r\n\r\n------WebKitFormBoundaryBA75PYgSLXXBSt2w\r\nContent-Disposition: form-data; name="end_commit_oid"\r\n\r\n\r\n------WebKitFormBoundaryBA75PYgSLXXBSt2w\r\nContent-Disposition: form-data; name="base_commit_oid"\r\n\r\n\r\n------WebKitFormBoundaryBA75PYgSLXXBSt2w\r\nContent-Disposition: form-data; name="comment_id"\r\n\r\n\r\n------WebKitFormBoundaryBA75PYgSLXXBSt2w--\r\n')

  # Check if the request was successful
  if [[ $? -eq 0 ]]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Request sent successfully!"
    # You can parse the response here if needed
  else
    echo "$(date '+%Y-%m-%d %H:%M:%S') - ERROR: Failed to send request!"
  fi
}

# Function to log status
log_status() {
  echo "$(date '+%Y-%m-%d %H:%M:%S') - Script running. Next request in $1 minutes."
}

# Main loop
echo "Starting GitHub request script..."
echo "Will send requests every 16 minutes and log status every minute."
echo "Press Ctrl+C to stop the script."

# Initialize time counter
counter=0

# Create a log file
log_file="github_request_log_$(date '+%Y%m%d_%H%M%S').txt"
echo "Log file: $log_file"
echo "Started at: $(date '+%Y-%m-%d %H:%M:%S')" > "$log_file"

# Run the initial request
send_request | tee -a "$log_file"

# Infinite loop
while true; do
  # Sleep for 1 minute
  sleep 60

  # Increment counter
  ((counter++))

  # Log to file and console
  if [ $counter -eq 16 ]; then
    # Reset counter
    counter=0

    # Send the request
    send_request | tee -a "$log_file"
  else
    # Log status
    log_status $((16 - counter)) | tee -a "$log_file"
  fi
done
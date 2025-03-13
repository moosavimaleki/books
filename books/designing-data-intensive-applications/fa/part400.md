میخوام برنامه در کنسول مرورگر بنویسم که مدام (هر ۵ ثانیه) در صفحه دنبال چنین عبارتی بگردد
<span>: we default stop the agent after 25 tool calls. Please ask the agent to continue manually.</span>


وقتی چنین چیزی دید پلن A را اجرا کند

وقتی چنین چیزی دید

<span>high load now.</span>


پلن ‌B را اجرا کند

---------------------------
توضیحات پلن A


دنبال چنین textbox ای بگردد:
<div autocapitalize="off" class="aislash-editor-input" contenteditable="true" spellcheck="false" style="resize: none; grid-area: 1 / 1 / 1 / 1; overflow: hidden; line-height: inherit; font-family: inherit; font-size: inherit; color: var(--vscode-input-foreground); background-color: transparent; display: block; outline: none; scrollbar-width: none; box-sizing: border-box; border: none; overflow-wrap: break-word; word-break: break-word; padding: 0px; user-select: text; white-space: pre-wrap;" data-lexical-editor="true" role="textbox" dir="rtl"</p></div>

 و سپس درون ان یک من از پیش تعیین شده بنویسد مثلا test
سپس دبنال دکمه ای زیر بگردد

<div class="composer-bar-button codebase-button" style="line-height: 150%; opacity: 0.5; color: var(--vscode-button-foreground); display: flex; align-items: center; position: relative; font-size: 10px; background: var(--vscode-button-background);">submit<span class="keybinding" style="margin-left: 4px; opacity: 0.6;"> ⏎</span></div>

و روی چنین دکمه ای کلیک کند


---------------------------


توضیحات پلن B

سپس دبنال دکمه ای زیر بگردد

<div class="composer-bar-button codebase-button" style="line-height: 150%; opacity: 0.5; color: var(--vscode-button-foreground); display: flex; align-items: center; position: relative; font-size: 10px; background: var(--vscode-button-background);">submit<span class="keybinding" style="margin-left: 4px; opacity: 0.6;"> ⏎</span></div>

و روی چنین دکمه ای کلیک کند




------------------


// برنامه بررسی متن و اجرای خودکار اکشن‌ها
function runAutomation() {
    // تابع پلن A - پیدا کردن تکست باکس، نوشتن متن و کلیک روی دکمه
    function planA() {
        console.log('در حال اجرای پلن A...');

        // پیدا کردن تکست باکس
        const textbox = document.querySelector('div.aislash-editor-input[contenteditable="true"]');

        if (textbox) {
            // نوشتن متن در تکست باکس
            textbox.textContent = 'test';

            // ایجاد یک رویداد input برای شبیه‌سازی تایپ کردن
            const inputEvent = new Event('input', { bubbles: true });
            textbox.dispatchEvent(inputEvent);

            console.log('متن در تکست باکس نوشته شد');

            // پیدا کردن دکمه submit و کلیک روی آن
            setTimeout(() => {
                const submitButton = document.querySelector('div.composer-bar-button.codebase-button');
                if (submitButton) {
                    submitButton.click();
                    console.log('دکمه submit کلیک شد');
                } else {
                    console.log('دکمه submit پیدا نشد');
                }
            }, 500); // کمی صبر می‌کنیم تا متن به درستی وارد شود
        } else {
            console.log('تکست باکس پیدا نشد');
        }
    }

    // تابع پلن B - فقط کلیک روی دکمه submit
    function planB() {
        console.log('در حال اجرای پلن B...');

        // پیدا کردن و کلیک روی دکمه submit
        const submitButton = document.querySelector('div.composer-bar-button.codebase-button');
        if (submitButton) {
            submitButton.click();
            console.log('دکمه submit کلیک شد');
        } else {
            console.log('دکمه submit پیدا نشد');
        }
    }

    // بررسی متن‌های مورد نظر در صفحه
    function checkPage() {
        // تبدیل HTML صفحه به متن
        const pageText = document.body.innerHTML;

        // بررسی برای پیام توقف بعد از ۲۵ فراخوانی ابزار
        if (pageText.includes('<span>: we default stop the agent after 25 tool calls. Please ask the agent to continue manually.</span>')) {
            console.log('پیام توقف بعد از ۲۵ فراخوانی ابزار پیدا شد');
            planA();
        }

        // بررسی برای پیام بار بالا
        if (pageText.includes('<span>high load now.</span>')) {
            console.log('پیام بار بالا پیدا شد');
            planB();
        }
    }

    // اجرای بررسی هر ۵ ثانیه
    setInterval(checkPage, 5000);

    // اجرای بررسی اولیه بلافاصله
    checkPage();

    console.log('برنامه خودکار شروع به کار کرد. بررسی هر ۵ ثانیه انجام می‌شود...');
}

// شروع برنامه
runAutomation();

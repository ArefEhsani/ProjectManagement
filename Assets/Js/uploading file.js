/* مقدار دهی متغیر ها */
var $fileInput = $('.file-input');
var $droparea = $('.file-drop-area');

// فعال کردن باکس انتخاب فایل
$fileInput.on('dragenter focus click', function () {
    $droparea.addClass('is-active');
});

// برگشتن به حالت اولیه
$fileInput.on('dragleave blur drop', function () {
    $droparea.removeClass('is-active');
});

// تغییر متن باکس به اسم فایل
$fileInput.on('change', function () {
    var filesCount = $(this)[0].files.length;
    var $textContainer = $(this).prev();

    if (filesCount === 1) {
        // اگر یک فایل انتخاب شده بود اسم همان فایل نمایش داده بشه
        var fileName = $(this).val().split('\\').pop();
        $textContainer.text(fileName);
    } else {
        // اگر تعداد بیش تر از یک فایل بود تعداد فایل هارا نمایش دهد
        $textContainer.text(filesCount + ' فایل انتخاب شده');
    }
});
document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('inputGroupFile04');
    const uploadForm = document.getElementById('uploadForm');

    fileInput.addEventListener('change', function() {
        uploadForm.submit();
    });
});

document.addEventListener("DOMContentLoaded", function () {

    document.querySelectorAll(".upload-form").forEach(form => {

        form.addEventListener("submit", async function (e) {
            e.preventDefault();

            const docId = this.dataset.doc;
            const fileInput = this.querySelector("input[type='file']");
            const file = fileInput.files[0];
            const button = this.querySelector("button");

            if (!file) {
                alert("Please select a file");
                return;
            }

            // UI loading state
            button.disabled = true;
            button.innerText = "Uploading...";

            const formData = new FormData();
            formData.append("file", file);

            const url = window.uploadConfig.baseUrl.replace("/0/", `/${docId}/`);
            try {
                const response = await fetch(url, {
                    method: "POST",
                    body: formData,
                    headers: {
                        "X-CSRFToken": getCSRFToken(),
                        "X-Requested-With": "XMLHttpRequest"
                    }
                });

                const data = await response.json();

                if (data.success) {

                    const card = this.closest(".doc-card");

                    card.innerHTML = `
                        <p><strong>${data.document.name}</strong></p>
                        <span class="done">✔ Uploaded</span>
                        <small>Uploaded successfully</small>
                    `;

                } else {
                    alert(data.error || "Upload failed");
                    button.disabled = false;
                    button.innerText = "Upload";
                }

            } catch (error) {
                console.error(error);
                alert("Server error");

                button.disabled = false;
                button.innerText = "Upload";
            }

        });

    });

});


// COOKIE-BASED CSRF (BEST PRACTICE)
function getCSRFToken() {
    return document.cookie
        .split("; ")
        .find(row => row.startsWith("csrftoken="))
        ?.split("=")[1];
}
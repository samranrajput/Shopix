document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("toggleCategories");
    const extraCategories = document.querySelectorAll(".hidden-category");
    const icon = toggleButton.querySelector("i"); // Get the <i> tag inside the button

    toggleButton.addEventListener("click", function () {
        extraCategories.forEach(category => {
            if (category.classList.contains("hidden-category")) {
                category.classList.remove("hidden-category");
                category.classList.add("visible-category");
            } else {
                category.classList.remove("visible-category");
                category.classList.add("hidden-category");
            }
        });

        // Toggle button text and arrow icon
        if (toggleButton.textContent.trim().startsWith("See All")) {
            toggleButton.innerHTML = '<strong>See Less</strong> <i class="bi bi-chevron-up"></i>';
        } else {
            toggleButton.innerHTML = '<strong>See All</strong> <i class="bi bi-chevron-down"></i>';
        }
    });
});

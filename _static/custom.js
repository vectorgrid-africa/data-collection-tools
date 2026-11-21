/* VectorGrid Documentation Custom JavaScript */

(function() {
    // Default to light theme when no user preference has been saved
    if (!localStorage.getItem('theme')) {
        localStorage.setItem('theme', 'light');
    }
    if (document.body && (!document.body.dataset.theme || document.body.dataset.theme === 'auto')) {
        document.body.dataset.theme = localStorage.getItem('theme') || 'light';
    }
})();

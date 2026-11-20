/* VectorGrid Documentation Custom JavaScript */

(function() {
    // Prevent RTD theme from auto-scrolling sidebar and hiding search/header on page load
    if (!window.location.hash) {
        var origScrollIntoView = Element.prototype.scrollIntoView;
        Element.prototype.scrollIntoView = function() {
            // If the element being scrolled is inside .wy-side-scroll and there is no URL hash, ignore
            if (!window.location.hash && this.closest && this.closest('.wy-side-scroll')) {
                return;
            }
            return origScrollIntoView.apply(this, arguments);
        };

        // Restore normal scrollIntoView after page load has completed
        window.addEventListener('load', function() {
            setTimeout(function() {
                Element.prototype.scrollIntoView = origScrollIntoView;
                var navScroll = document.querySelector('.wy-side-scroll');
                if (navScroll && !window.location.hash) {
                    navScroll.scrollTop = 0;
                }
            }, 100);
        });
    }
})();

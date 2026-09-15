(function () {
  var KEY = "atlas_build_loop_theme_v1";
  function apply(mode) {
    document.documentElement.setAttribute("data-theme", mode === "dim" ? "dim" : "light");
    try { localStorage.setItem(KEY, mode === "dim" ? "dim" : "light"); } catch (e) {}
    document.querySelectorAll("[data-theme-toggle]").forEach(function (btn) {
      btn.textContent = mode === "dim" ? "Bright mode" : "Dim mode";
    });
  }
  var start = "light";
  try { start = localStorage.getItem(KEY) || "light"; } catch (e) {}
  apply(start);
  document.addEventListener("click", function (ev) {
    var t = ev.target;
    if (!t || !t.getAttribute || !t.hasAttribute("data-theme-toggle")) return;
    var cur = document.documentElement.getAttribute("data-theme") === "dim" ? "dim" : "light";
    apply(cur === "dim" ? "light" : "dim");
  });
})();

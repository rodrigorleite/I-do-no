document.addEventListener("DOMContentLoaded", () => {
    const celular = document.querySelector(".celular");
    const menuLateral = document.querySelector(".menu-lateral");
    const header = document.querySelector("header");

    if (!celular || !menuLateral) {
        console.error("Elemento do menu ou ícone celular não encontrado no DOM.");
        return;
    }

    // Torna o cabeçalho fixo no topo da página
    if (header) {
        header.style.position = "fixed";
        header.style.top = "0";
        header.style.left = "0";
        header.style.width = "100%";
        header.style.zIndex = "999";
    }

    function showLinksSequentially() {
        const links = menuLateral.querySelectorAll("li");
        links.forEach((link, i) => {
            setTimeout(() => {
                link.classList.add("mostrar");
            }, 150 * i);
        });
    }

    function hideLinksSequentially() {
        const links = menuLateral.querySelectorAll("li");
        const total = links.length;
        links.forEach((link, i) => {
            setTimeout(() => {
                link.classList.remove("mostrar");
            }, 100 * (total - 1 - i));
        });
    }

    function abrirMenu() {
        menuLateral.classList.add("mostrarMenu");
        document.body.classList.add("menu-aberto");
        showLinksSequentially();
    }

    function fecharMenu() {
        hideLinksSequentially();
        const totalDelay = 100 * menuLateral.querySelectorAll("li").length + 300;
        setTimeout(() => {
            menuLateral.classList.remove("mostrarMenu");
            document.body.classList.remove("menu-aberto");
        }, totalDelay);
    }

    celular.addEventListener("click", (e) => {
        e.stopPropagation();
        if (menuLateral.classList.contains("mostrarMenu")) {
            fecharMenu();
        } else {
            abrirMenu();
        }
    });

    document.addEventListener("click", (e) => {
        if (!menuLateral.contains(e.target) && e.target !== celular) {
            fecharMenu();
        }
    });

    menuLateral.addEventListener("click", () => {
        fecharMenu();
    });
});
(function () {
  const KEY = 'gt_favs';

  function slugify(text) {
    return text.toString().toLowerCase().trim()
      .normalize('NFD').replace(/[\u0300-\u036f]/g, '') // eliminar acentos
      .replace(/\s+/g, '-').replace(/[^\w-]/g, '');
  }

  function loadFavs() {
    try {
      return JSON.parse(localStorage.getItem(KEY) || '[]');
    } catch (e) {
      return [];
    }
  }
  function saveFavs(arr) {
    localStorage.setItem(KEY, JSON.stringify(arr));
  }

  function getCardData(card) {
    const titleEl = card.querySelector('.card-title');
    const imgEl = card.querySelector('.card-img');
    const linkEl = card.querySelector('.card-link');
    const title = titleEl ? titleEl.innerText.trim() : 'Receta';
    const img = imgEl ? imgEl.getAttribute('src') : '';
    const href = linkEl ? linkEl.getAttribute('href') : '#';
    const id = slugify(title);
    return { id, title, img, href };
  }

  function isFav(id) {
    return loadFavs().some(r => r.id === id);
  }

  function setHeartState(btn, state) {
    btn.classList.toggle('is-fav', state);
    btn.setAttribute('aria-pressed', state ? 'true' : 'false');
    btn.innerText = state ? '♥' : '♡';
  }

  // Toggle cuando se hace click en corazón de una card normal
  function handleHeartClick(ev) {
    const btn = ev.currentTarget;
    const card = btn.closest('.card');
    const item = getCardData(card);
    const favs = loadFavs();
    const exists = favs.findIndex(r => r.id === item.id);
    if (exists === -1) {
      favs.push(item);
      saveFavs(favs);
      setHeartState(btn, true);
    } else {
      favs.splice(exists, 1);
      saveFavs(favs);
      setHeartState(btn, false);
    }
    // si estamos en favoritos.html, volver a renderizar la lista
    if (document.getElementById('favorites-list')) renderFavorites();
  }

  // Inicializar corazones en páginas de recetas/listas
  function initHearts() {
    const hearts = document.querySelectorAll('.card .heart');
    hearts.forEach(btn => {
      const card = btn.closest('.card');
      const item = getCardData(card);
      setHeartState(btn, isFav(item.id));
      btn.addEventListener('click', handleHeartClick);
    });
  }

  // --- FAVORITOS PAGE ---
  function createFavCard(obj) {
    const article = document.createElement('article');
    article.className = 'card fav-card';
    article.innerHTML = `
      <button class="heart" aria-label="Quitar favorito">♥</button>
      <img src="${obj.img}" alt="${obj.title}" class="card-img">
      <div class="card-body">
        <h3 class="card-title">${obj.title}</h3>
        <a href="${obj.href}" class="card-link">Ver receta</a>
      </div>
    `;
    // corazón de la lista también quita
    const heart = article.querySelector('.heart');
    heart.addEventListener('click', () => {
      const favs = loadFavs().filter(r => r.id !== obj.id);
      saveFavs(favs);
      renderFavorites();
      // también actualizar corazones en otras páginas si existen
      document.querySelectorAll('.card .card-title').forEach(t => {
        if (t.innerText.trim() === obj.title) {
          const h = t.closest('.card').querySelector('.heart');
          if (h) setHeartState(h, false);
        }
      });
    });
    return article;
  }

  function renderFavorites() {
    const container = document.getElementById('favorites-list');
    if (!container) return;
    container.innerHTML = '';
    const favs = loadFavs();
    if (!favs.length) {
      const p = document.createElement('p');
      p.className = 'empty';
      p.innerText = 'No tienes recetas en Favoritos. Pulsa ♡ en una receta para añadirla.';
      container.appendChild(p);
      return;
    }
    const grid = document.createElement('div');
    grid.className = 'fav-grid';
    favs.forEach(f => grid.appendChild(createFavCard(f)));
    container.appendChild(grid);
  }

  document.addEventListener('DOMContentLoaded', () => {
    initHearts();
    if (document.getElementById('favorites-list')) renderFavorites();
  });

})();

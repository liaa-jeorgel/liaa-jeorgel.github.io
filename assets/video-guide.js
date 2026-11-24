/* Capítulos progressivos: links temporais nativos sem JavaScript. */
(() => {
  const video = document.querySelector('#project-video');
  if (!video) return;
  const chapterTrack = video.querySelector('track[kind="chapters"]');
  if (chapterTrack?.track) chapterTrack.track.mode = 'hidden';
  const links = [...document.querySelectorAll('[data-video-time]')];
  const status = document.querySelector('#video-chapter-status');
  const fullscreen = document.querySelector('.video-fullscreen');
  let request = 0;
  let active = -1;
  function updateChapter() {
    let index = 0;
    links.forEach((link,i) => {if (video.currentTime >= Number(link.dataset.videoTime)-.05) index = i;});
    if (active === index) return;
    active = index;
    links.forEach((link,i) => {
      if (i === index) link.setAttribute('aria-current','step');
      else link.removeAttribute('aria-current');
    });
  }
  links.forEach(link => link.addEventListener('click', event => {
    if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    const time = Number(link.dataset.videoTime);
    if (!Number.isFinite(time)) return;
    const token = ++request;
    status.textContent = 'A preparar o capítulo seleccionado…';
    function seek() {
      if (token !== request) return;
      video.currentTime = Math.min(time, Math.max(0,video.duration-.1));
      status.textContent = `Capítulo: ${link.querySelector('strong').textContent}. Use o leitor para reproduzir.`;
      updateChapter();
    }
    if (video.readyState >= 1) seek();
    else {video.addEventListener('loadedmetadata',seek,{once:true});video.load();}
  }));
  video.addEventListener('timeupdate',updateChapter);
  video.addEventListener('seeked',updateChapter);
  video.addEventListener('loadedmetadata',updateChapter);
  video.addEventListener('error',() => {status.textContent = 'Não foi possível carregar o vídeo. Use a transcrição ou a ligação para descarregar.';});
  if (video.requestFullscreen || video.webkitEnterFullscreen) {
    fullscreen.hidden = false;
    fullscreen.addEventListener('click',async () => {
      try {
        if (video.requestFullscreen) await video.requestFullscreen();
        else video.webkitEnterFullscreen();
      } catch {status.textContent = 'Use o controlo de ecrã inteiro do leitor.';}
    });
  }
})();

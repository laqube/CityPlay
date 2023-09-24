const video = document.getElementById('camera');
const cheeseBtn = document.getElementById('cheese-btn');
const snapshot = document.getElementById('snapshot');

navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(err => {
        console.error('Error accessing the camera', err);
    });

cheeseBtn.addEventListener('click', () => {
    const countdown = document.createElement('div');
    countdown.style.position = 'absolute';
    countdown.style.left = '50%';
    countdown.style.top = '50%';
    countdown.style.transform = 'translate(-50%, -50%)';
    countdown.style.fontSize = '48px';
    countdown.style.color = 'white';
    document.getElementById('camera-container').appendChild(countdown);

    let count = 3;
    countdown.innerText = count;

    const interval = setInterval(() => {
        count--;
        if (count === 0) {
            clearInterval(interval);
            countdown.remove();

            const canvas = document.createElement('canvas');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
            snapshot.src = canvas.toDataURL('image/png');
        } else {
            countdown.innerText = count;
        }
    }, 1000);
});

function toggle_visibility(id) {
    var e = document.getElementById(id);
    if (e.style.display == 'block') {
        setTimeout(function() {
            e.style.display = 'none';
        }, 3000); // 3 seconds delay
    } else {
        setTimeout(function() {
            e.style.display = 'block';
        }, 3000); // 3 seconds delay
    }
}
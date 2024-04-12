function fetchMetrics() {
    fetch('/metrics')
        .then(response => response.json())
        .then(data => {
            document.getElementById('cpu_load').textContent = data.cpu_load + '%';
            document.getElementById('ram_used').textContent = data.ram_used.toFixed(2) + ' GB';
            document.getElementById('ram_total').textContent = data.ram_total.toFixed(2) + ' GB';

            const drivesContainer = document.getElementById('drives_container');
            drivesContainer.innerHTML = '';  // Clear existing content
            data.drive_metrics.forEach(drive => {
                const p = document.createElement('p');
                p.className = 'metric';
                p.innerHTML = `${drive.label} Used: <span>${drive.used.toFixed(2)} GB</span> / ${drive.total.toFixed(2)} GB`;
                drivesContainer.appendChild(p);
            });
        })
        .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function() {
    fetchMetrics();
    setInterval(fetchMetrics, 5000);
});

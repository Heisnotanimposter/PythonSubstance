document.addEventListener('DOMContentLoaded', () => {
    // Example data for rankings
    const citationPapers = [
        "Deep Learning - 32,000 citations",
        "Transformers - 25,500 citations",
        "Attention Is All You Need - 21,800 citations"
    ];
    const dailyViews = ["GANs - 500 views", "YOLO - 450 views", "ResNet - 420 views"];
    const weeklyViews = ["CNNs - 3500 views", "RNNs - 3300 views", "ViTs - 3100 views"];
    const monthlyViews = ["GPT-4 - 12,000 views", "BERT - 11,500 views", "Diffusion Models - 10,800 views"];

    const newsArticles = [
        "New AI Models Solve Protein Folding - [Link]",
        "Quantum Computing in 2024 - [Link]"
    ];

    const youtubeArticles = [
        "Top 5 AI Breakthroughs in 2024 - [Watch Video]",
        "Neural Networks Explained - [Watch Video]"
    ];

    // Populate lists
    populateList('citations-list', citationPapers);
    populateList('daily-views-list', dailyViews);
    populateList('weekly-views-list', weeklyViews);
    populateList('monthly-views-list', monthlyViews);
    populateList('news-list', newsArticles);
    populateList('youtube-list', youtubeArticles);

    // Populate list function
    function populateList(elementId, data) {
        const list = document.getElementById(elementId);
        data.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item;
            list.appendChild(li);
        });
    }

    // Contact form handler
    document.getElementById("contactForm").addEventListener("submit", function (e) {
        e.preventDefault();

        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const message = document.getElementById("message").value;

        if (name && email && message) {
            alert(`Thank you, ${name}! Your message has been sent.`);
            document.getElementById("contactForm").reset();
        } else {
            alert("Please fill out all fields.");
        }
    });
});
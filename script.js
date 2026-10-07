document.addEventListener('DOMContentLoaded', () => {
    const analyzeBtn = document.getElementById('analyzeBtn');
    const newsInput = document.getElementById('newsInput');
    const loadingSection = document.getElementById('loading');
    const resultSection = document.getElementById('result');
    const predictionBox = document.getElementById('prediction');
    const confidenceText = document.getElementById('confidence');

    analyzeBtn.addEventListener('click', () => {
        const text = newsInput.value.trim();

        if (!text) {
            alert('Please enter some text to analyze.');
            return;
        }

        // Hide result, show loading, disable button
        resultSection.classList.add('hidden');
        loadingSection.classList.remove('hidden');
        analyzeBtn.disabled = true;

        // Simulate API call and ML model prediction delay
        setTimeout(() => {
            // Mock prediction logic (random for demonstration)
            // In a real app, you would make a fetch() request to your ML backend here
            const isReal = Math.random() > 0.5;
            const confidence = (Math.random() * 20 + 80).toFixed(2); // Random confidence between 80-100%

            // Update UI with results
            loadingSection.classList.add('hidden');
            resultSection.classList.remove('hidden');
            analyzeBtn.disabled = false;

            // Reset classes
            predictionBox.className = 'prediction-box';

            if (isReal) {
                predictionBox.textContent = 'REAL NEWS';
                predictionBox.classList.add('real');
            } else {
                predictionBox.textContent = 'FAKE NEWS';
                predictionBox.classList.add('fake');
            }

            confidenceText.textContent = `Confidence Score: ${confidence}%`;

        }, 1500); // 1.5 second simulated delay
    });
});

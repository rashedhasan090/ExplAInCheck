// ExplAInCheck Frontend Application with Chart.js Integration
// const API_BASE_URL = 'http://localhost:5001/api';
const API_BASE_URL = 'https://explaincheck.onrender.com/api';


// Chart instances (global to allow updates)
let statusChart, confidenceChart, radarChart;

document.addEventListener('DOMContentLoaded', () => {
    const verifyBtn = document.getElementById('verify-btn');
    const clearBtn = document.getElementById('clear-btn');
    const randomDemoBtn = document.getElementById('random-demo-btn');
    const explanationInput = document.getElementById('explanation-input');
    const resultsSection = document.getElementById('results-section');
    const loading = document.getElementById('loading');
    
    // Event Listeners
    verifyBtn.addEventListener('click', verifyExplanation);
    clearBtn.addEventListener('click', clearForm);
    randomDemoBtn.addEventListener('click', loadRandomDemo);
    
    // Enter key to verify
    explanationInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && e.ctrlKey) {
            verifyExplanation();
        }
    });
});

async function loadRandomDemo() {
    const loading = document.getElementById('loading');
    const explanationInput = document.getElementById('explanation-input');
    
    try {
        loading.style.display = 'flex';
        
        const response = await fetch(`${API_BASE_URL}/random-demo`);
        const data = await response.json();
        
        if (data.success && data.demo) {
            explanationInput.value = data.demo.explanation;
            
            // Show a notification about the loaded demo
            showNotification(`Loaded: ${data.demo.title}`, 'info');
        }
        
    } catch (error) {
        console.error('Error loading demo:', error);
        showNotification('Failed to load demo. Using fallback example.', 'error');
        
        // Fallback demo
        explanationInput.value = "You should water banana plants at 5pm because the soil is cooler, leading to less evaporation. Given that banana plants need consistent moisture levels and current soil readings show 40% capacity, increase watering to 50mm per week during flowering stage.";
    } finally {
        loading.style.display = 'none';
    }
}

async function verifyExplanation() {
    const explanationInput = document.getElementById('explanation-input');
    const domainSelect = document.getElementById('domain-select');
    const loading = document.getElementById('loading');
    const resultsSection = document.getElementById('results-section');
    const verifyBtn = document.getElementById('verify-btn');
    
    const explanation = explanationInput.value.trim();
    const domain = domainSelect.value;
    
    if (!explanation) {
        alert('Please enter an explanation to verify.');
        return;
    }
    
    // Show loading
    loading.style.display = 'flex';
    verifyBtn.disabled = true;
    resultsSection.style.display = 'none';
    
    try {
        const response = await fetch(`${API_BASE_URL}/verify`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ explanation, domain })
        });
        
        const data = await response.json();
        displayResults(data);
        
    } catch (error) {
        console.error('Error:', error);
        alert('Error connecting to API. Make sure backend is running on port 5001.');
    } finally {
        loading.style.display = 'none';
        verifyBtn.disabled = false;
    }
}

function displayResults(data) {
    const resultsSection = document.getElementById('results-section');
    
    // Show results section
    resultsSection.style.display = 'block';
    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    
    // Display similarity match if found
    displaySimilarityMatch(data.similarity_match);
    
    // Display overall status
    displayOverallStatus(data.overall_status, data.summary);
    
    // Display metrics
    displayMetrics(data.metrics);
    
    // Render charts
    renderCharts(data.chart_data);
    
    // Display recommendations
    displayRecommendations(data.recommendations);
    
    // Display detailed claims
    displayClaims(data.claims);
}

function displaySimilarityMatch(similarityMatch) {
    const banner = document.getElementById('similarity-banner');
    const score = document.getElementById('similarity-score');
    const message = document.getElementById('similarity-message');
    
    if (similarityMatch && similarityMatch.found) {
        banner.style.display = 'block';
        score.textContent = `${similarityMatch.similarity_score}% Match Found`;
        message.textContent = `Matched with: ${similarityMatch.matched_scenario}. ${similarityMatch.recommendation}`;
        banner.className = 'similarity-banner match-found';
    } else if (similarityMatch && !similarityMatch.found) {
        banner.style.display = 'block';
        score.textContent = 'Novel Scenario';
        message.textContent = similarityMatch.message;
        banner.className = 'similarity-banner novel-scenario';
    } else {
        banner.style.display = 'none';
    }
}

function displayOverallStatus(status, summary) {
    const statusBadge = document.getElementById('overall-status');
    const summaryText = document.getElementById('summary-text');
    
    statusBadge.textContent = status.charAt(0).toUpperCase() + status.slice(1);
    statusBadge.className = `status-badge status-${status}`;
    summaryText.textContent = summary;
}

function displayMetrics(metrics) {
    document.getElementById('metric-data-quality').textContent = `${metrics.data_quality}%`;
    document.getElementById('metric-logical').textContent = `${metrics.logical_consistency}%`;
    document.getElementById('metric-completeness').textContent = `${metrics.completeness}%`;
    document.getElementById('metric-evidence').textContent = `${metrics.evidence_strength}%`;
    document.getElementById('metric-relevance').textContent = `${metrics.contextual_relevance}%`;
    
    // Add color coding
    const metricElements = document.querySelectorAll('.metric-value');
    metricElements.forEach(el => {
        const value = parseInt(el.textContent);
        if (value >= 75) el.style.color = '#4caf50';
        else if (value >= 50) el.style.color = '#ff9800';
        else el.style.color = '#f44336';
    });
}

function renderCharts(chartData) {
    if (!chartData) return;
    
    // Destroy existing charts
    if (statusChart) statusChart.destroy();
    if (confidenceChart) confidenceChart.destroy();
    if (radarChart) radarChart.destroy();
    
    // Status Distribution Pie Chart
    const statusCtx = document.getElementById('statusChart').getContext('2d');
    statusChart = new Chart(statusCtx, {
        type: 'pie',
        data: {
            labels: ['Valid', 'Invalid', 'Questionable'],
            datasets: [{
                data: [
                    chartData.status_distribution.valid,
                    chartData.status_distribution.invalid,
                    chartData.status_distribution.questionable
                ],
                backgroundColor: ['#4caf50', '#f44336', '#ff9800']
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: 'bottom' }
            }
        }
    });
    
    // Confidence Distribution Bar Chart
    const confidenceCtx = document.getElementById('confidenceChart').getContext('2d');
    confidenceChart = new Chart(confidenceCtx, {
        type: 'bar',
        data: {
            labels: ['High (75%+)', 'Medium (45-75%)', 'Low (<45%)'],
            datasets: [{
                label: 'Number of Claims',
                data: [
                    chartData.confidence_distribution.high,
                    chartData.confidence_distribution.medium,
                    chartData.confidence_distribution.low
                ],
                backgroundColor: ['#4caf50', '#ff9800', '#f44336']
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false }
            },
            scales: {
                y: { beginAtZero: true, ticks: { stepSize: 1 } }
            }
        }
    });
    
    // Metrics Radar Chart
    const radarCtx = document.getElementById('radarChart').getContext('2d');
    radarChart = new Chart(radarCtx, {
        type: 'radar',
        data: {
            labels: chartData.metrics_radar.labels,
            datasets: [{
                label: 'Quality Metrics',
                data: chartData.metrics_radar.values,
                backgroundColor: 'rgba(76, 175, 80, 0.2)',
                borderColor: '#4caf50',
                pointBackgroundColor: '#4caf50'
            }]
        },
        options: {
            responsive: true,
            scales: {
                r: {
                    beginAtZero: true,
                    max: 100,
                    ticks: { stepSize: 20 }
                }
            }
        }
    });
}

function displayRecommendations(recommendations) {
    const list = document.getElementById('recommendations-list');
    list.innerHTML = '';
    
    if (recommendations && recommendations.length > 0) {
        recommendations.forEach(rec => {
            const li = document.createElement('li');
            li.textContent = rec;
            list.appendChild(li);
        });
    } else {
        list.innerHTML = '<li>No specific recommendations at this time.</li>';
    }
}

function displayClaims(claims) {
    const claimsList = document.getElementById('claims-list');
    claimsList.innerHTML = '';
    
    if (claims && claims.length > 0) {
        claims.forEach(claim => {
            const claimCard = document.createElement('div');
            claimCard.className = 'claim-card';
            
            const statusClass = `status-${claim.status}`;
            
            claimCard.innerHTML = `
                <div class="claim-header">
                    <span class="claim-status ${statusClass}">${claim.status}</span>
                    <span class="claim-confidence">${claim.confidence}% confidence</span>
                </div>
                <p class="claim-text">${claim.claim}</p>
                <p class="claim-reasoning"><strong>Reasoning:</strong> ${claim.reasoning}</p>
            `;
            
            claimsList.appendChild(claimCard);
        });
    } else {
        claimsList.innerHTML = '<p>No claims analyzed.</p>';
    }
}

function clearForm() {
    document.getElementById('explanation-input').value = '';
    document.getElementById('results-section').style.display = 'none';
}

function showNotification(message, type = 'info') {
    // Simple notification (you can enhance this with a library)
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 20px;
        background: ${type === 'error' ? '#f44336' : '#2196f3'};
        color: white;
        border-radius: 4px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        z-index: 10000;
        animation: slideIn 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

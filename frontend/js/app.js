import { ApiClient } from './api_client.js';
import { UiRenderer } from './ui_renderer.js';

const api = new ApiClient();
const ui = new UiRenderer();

document.addEventListener('DOMContentLoaded', async () => {
    console.log('DrillCalc App Initialized');

    // Check API Status
    const statusEl = document.getElementById('api-status');
    const isOnline = await api.checkHealth();
    if (isOnline) {
        statusEl.textContent = 'API: ONLINE';
        statusEl.style.color = 'var(--status-safe)';
    } else {
        statusEl.textContent = 'API: OFFLINE';
        statusEl.style.color = 'var(--status-danger)';
    }

    // Handle Navigation
    document.querySelectorAll('.nav-item').forEach(item => {
        item.addEventListener('click', () => {
            const viewId = item.getAttribute('data-view');
            const title = item.querySelector('span:not(.nav-icon)').textContent;
            ui.switchView(viewId, title);
        });
    });

    // Handle Hoisting Form Submit
    const hoistingForm = document.getElementById('calc-form');
    hoistingForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        ui.clearErrors('hoisting');

        const formData = new FormData(hoistingForm);
        const inputData = {
            hook_load: parseFloat(formData.get('hook_load')),
            lines: parseInt(formData.get('lines')),
            sheaves: parseInt(formData.get('sheaves')),
            friction_factor: parseFloat(formData.get('friction_factor')),
            wire_strength: parseFloat(formData.get('wire_strength'))
        };

        try {
            const results = await api.calculateHoisting(inputData);
            ui.updateSafetyCard(results.safety_factor, results.alert_level);
            ui.updateMetrics(results);
            ui.updateDerrickLoad(results);
        } catch (error) {
            ui.showError(error.message, 'hoisting');
        }
    });

    // Handle Ton-Mile Form Submit
    const tonMileForm = document.getElementById('ton-mile-form');
    tonMileForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        ui.clearErrors('ton-mile');

        const formData = new FormData(tonMileForm);
        const inputData = {
            depth: parseFloat(formData.get('depth')),
            stand_length: parseFloat(formData.get('stand_length')),
            pipe_weight_mud: parseFloat(formData.get('pipe_weight_mud')),
            block_weight: parseFloat(formData.get('block_weight')),
            collar_weight_mud: parseFloat(formData.get('collar_weight_mud')),
            collar_length: parseFloat(formData.get('collar_length'))
        };

        try {
            const results = await api.calculateTonMile(inputData);
            ui.updateTonMileResult(results.ton_miles);
        } catch (error) {
            ui.showError(error.message, 'ton-mile');
        }
    });
});


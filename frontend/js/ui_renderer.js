/**
 * DrillCalc - Module 1: Hoisting System & Structure
 * Author: Antony Picon, Mechanical Engineer
 * Description: UI Rendering module for DOM manipulation.
 */
/**
 * UI Renderer for DrillCalc
 * Defines functions to update the DOM based on calculation results.
 */

export class UiRenderer {

    constructor() {
        // Cache DOM elements if needed, or select dynamic
    }

    /**
     * Formats a number with commas and decimals.
     * @param {number} num 
     * @param {number} decimals 
     */
    formatNumber(num, decimals = 2) {
        if (num === undefined || num === null) return '--';
        return num.toLocaleString('en-US', {
            minimumFractionDigits: decimals,
            maximumFractionDigits: decimals
        });
    }

    updateSafetyCard(fd, alertLevel) {
        const card = document.getElementById('safety-card');
        const valueEl = document.getElementById('fd-value');
        const statusEl = document.getElementById('fd-status');

        // Reset classes
        card.classList.remove('safe', 'caution', 'danger');

        // Add new class based on alert level (mapped to lowercase)
        const levelClass = alertLevel.toLowerCase();
        card.classList.add(levelClass);

        valueEl.textContent = this.formatNumber(fd, 2);

        // Translate status
        const statusMap = {
            'SAFE': 'OPERACIÓN SEGURA',
            'CAUTION': 'PRECAUCIÓN',
            'DANGER': 'PELIGRO CRÍTICO'
        };
        statusEl.textContent = statusMap[alertLevel] || alertLevel;
    }

    updateMetrics(data) {
        // Efficiency (show as percentage)
        const effPercent = data.efficiency * 100;
        document.getElementById('efficiency-value').textContent = this.formatNumber(effPercent, 1);

        document.getElementById('fast-line-value').textContent = this.formatNumber(data.fast_line_tension, 0);
        document.getElementById('dead-line-value').textContent = this.formatNumber(data.dead_line_load, 0);
    }

    updateDerrickLoad(data) {
        const element = document.getElementById('derrick-load-value');
        element.textContent = this.formatNumber(data.derrick_load, 0);

        // Simple visual bar animation based on an arbitrary max load (e.g. 2,000,000 lbs ?) 
        // In a real app we might compare against Rig Capacity (not yet in input).
        // For now, we just fill it to look cool/alive.
        const bar = document.getElementById('load-bar');

        // Reset to trigger animation
        bar.style.width = '0%';
        setTimeout(() => {
            bar.style.width = '75%'; // Static visual or dynamic if we knew capacity
        }, 100);
    }

    clearErrors() {
        document.getElementById('form-error').textContent = '';
    }

    showError(msg) {
        document.getElementById('form-error').textContent = `⚠️ ${msg}`;
    }
}

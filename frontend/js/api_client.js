/**
 * DrillCalc - Module 1: Hoisting System & Structure
 * Author: Antony Picon, Mechanical Engineer
 * Description: API client module for backend communication.
 */
/**
 * ApiClient for DrillCalc Module 1
 * Handles communication with the FastAPI backend.
 */
export class ApiClient {
    constructor(baseUrl = 'http://localhost:8000') {
        this.baseUrl = baseUrl;
    }

    /**
     * Sends calculation request to the backend.
     * @param {Object} inputData - The data collected from the form.
     * @returns {Promise<Object>} - The JSON response from the server.
     */
    async calculateHoisting(inputData) {
        const url = `${this.baseUrl}/module-1/calculate`;

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify(inputData)
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Error en la solicitud al servidor');
            }

            return await response.json();

        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }

    /**
     * Checks if the API is reachable.
     */
    async checkHealth() {
        try {
            const response = await fetch(`${this.baseUrl}/`);
            return response.ok;
        } catch (e) {
            return false;
        }
    }
}

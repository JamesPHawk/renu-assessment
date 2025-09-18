import { describe, it, expect } from "vitest";

// Update this to match your Flask server URL
const API_URL = "http://127.0.0.1:5000/renu-fibonacci";

async function callFibonacciAPI(value: number) {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ value }),
    });

    return response.json();
    }

    describe("Fibonacci API integration tests", () => {
        it("should return Fibonacci(1) = 1", async () => {
            const data = await callFibonacciAPI(1);
            expect(data.value).toBe(1);
        });

        it("should return Fibonacci(10) = 55", async () => {
            const data = await callFibonacciAPI(10);
            expect(data.value).toBe(55);
        });

        
        it("should return Fibonacci(70) = 1.90e+14", async () => {
            const data = await callFibonacciAPI(70);
            expect(data.value).toBe("1.90e+14");
        });

        it("should return Fibonacci(1001) = 7.03e+208", async () => {
            const data = await callFibonacciAPI(1001);
            expect(data.value).toBe("7.03e+208");
        });

        it("should return Fibonacci(-1) = 1", async () => {
            const data = await callFibonacciAPI(-1);
            expect(data.value).toBe(1);
        });

    describe("Internal Server Error test", () => {
        it("should throw Internal Server Error for very large positive input", async () => {
            const response = await callFibonacciAPI(100000000);
            expect(response.status).toBe(500);
        });
    });
}
);

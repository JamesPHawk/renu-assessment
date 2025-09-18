import { test, expect } from '@playwright/test';

test('fibonacci-app-test', async ({ page }) => {
  await page.goto('http://localhost:4173/');
  await expect(page.getByText('This calculator will find the')).toBeVisible();
  await page.getByRole('textbox', { name: 'Index (n)' }).click();
  await page.getByRole('textbox', { name: 'Index (n)' }).fill('12');
  await page.getByRole('button', { name: 'Submit' }).click();
  await expect(page.locator('#app')).toContainText('F(12) = 144');
  await page.getByRole('textbox', { name: 'Index (n)' }).fill('-1000');
  await page.getByRole('button', { name: 'Submit' }).click();
  await expect(page.locator('#app')).toContainText('Number is out of range');
  await page.getByRole('textbox', { name: 'Index (n)' }).fill('10');
  await page.getByRole('button', { name: 'Submit' }).click();
  await expect(page.getByRole('rowgroup')).toContainText('10');
  await expect(page.getByRole('rowgroup')).toContainText('55');
});
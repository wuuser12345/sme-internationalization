# Firm Size and Firm Performance

### Research Note Project | SS 2026 Dilara

## Research Question

Does firm size have a positive linear relationship with firm performance among European firms?

## Theoretical Background

The hypothesis is based on the resource-based view of the firm and arguments related to economies of scale. Larger firms usually have access to more financial, organizational and managerial resources. These resources can help firms operate more efficiently, invest in productive assets and spread fixed costs over a larger output base. Therefore, firm size may be associated with better firm performance.

At the same time, firm size is not automatically beneficial, because larger firms may also face higher coordination costs and more complex organizational structures. However, for this research note, the focus is on testing the simple linear expectation that larger firms perform better.

## Hypothesis

- H1: Firm size is positively associated with firm performance.

## Data

The analysis uses firm-level data from WRDS / Compustat Global. Firm performance is measured as return on assets (ROA), calculated as net income divided by total assets (NI / AT). Firm size is measured as the logarithm of total assets, log(AT).

## Empirical Strategy

The hypothesis will be tested using a simple linear regression model in Python:

ROA = beta0 + beta1 Firm Size + error

## Project Structure

The project follows a reproducible research setup with separate folders for raw data, processed data, code, output, references and the final research note.

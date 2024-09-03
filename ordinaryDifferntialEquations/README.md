```mermaid
flowchart TD
    A[Start] --> B[Initialize x, y, h, n]
    B --> C{Is i < n?}
    C -->|Yes| D[Calculate dy = x * y]
    D --> E[Update y = y + dy * h]
    E --> F[Update x = x + h]
    F --> G[Print x, y]
    G --> H[Increment i by 1]
    H --> C
    C -->|No| I[End]
```

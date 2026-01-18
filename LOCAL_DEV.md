# Running the Website Locally (macOS)

## Quick Start with Docker (Recommended)

1. **Navigate to your project directory:**
   ```bash
   cd /Users/qing/Documents/my_venv/zqypku.github.io
   ```

2. **Pull and start the Docker container:**
   ```bash
   docker compose pull
   docker compose up
   ```

3. **Open your browser:**
   - Go to `http://localhost:8080`
   - You should see your website running!

4. **Making changes:**
   - Edit any files in the project
   - The site will automatically rebuild (watch the terminal for updates)
   - Refresh your browser to see changes

5. **Stop the server:**
   - Press `Ctrl+C` in the terminal

## Alternative: Using Docker with Slim Image (Smaller Size)

If you want a smaller Docker image:

```bash
docker compose -f docker-compose-slim.yml pull
docker compose -f docker-compose-slim.yml up
```

## Troubleshooting

### If Docker commands don't work:
- Make sure Docker Desktop is running (check the menu bar for the Docker icon)
- Try: `docker compose up --build` to rebuild the image

### View logs:
```bash
docker compose logs
```

### Access the container shell:
```bash
docker compose exec -it jekyll /bin/bash
```

### Port already in use?
If port 8080 is already in use, edit `docker-compose.yml` and change:
```yaml
ports:
  - 8080:8080  # Change the first number to another port (e.g., 8081)
```

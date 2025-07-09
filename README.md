# game1 --- WIP

A cross-platform game built with Python.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
python main.py
```

## Development

### Project Structure
- `src/` - Source code
- `assets/` - Game assets (graphics, audio, etc.)
- `tests/` - Unit and integration tests
- `tools/` - Development tools and scripts
- `docs/` - Documentation

### Building

#### Desktop
```bash
python tools/scripts/build.py desktop
```

#### Web
```bash
python tools/scripts/build.py web
```

#### Mobile (Android)
```bash
python tools/scripts/build.py android
```

## Contributing

1. Follow PEP 8 style guidelines
2. Write tests for new features
3. Update documentation as needed

## License

MIT License - see LICENSE file for details.

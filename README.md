# Detection Demo for MIT-Hackathon

Step 1. Start inference server on a machine which `nvidia-docker` is correctly configured.

```bash
bash start_server.sh
```

Step 2. Run `main.py` to detect objects of `test.jpg`.

```bash
python main.py
```

Step 3. Check the `result.jpg`

```bash
open result.jpg
``` 

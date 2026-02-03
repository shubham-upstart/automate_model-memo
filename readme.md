1. **Start the EC2 + connect**
2. **Activate env + repo**
3. **Refresh CodeArtifact (occasionally)**
4. **Run your script**

---

## 1) Start the EC2 and connect

On your laptop:

1. In the AWS console, make sure the instance `i-075873fcacae06ca4` is **Running**.
2. In a terminal on your laptop:

   ```bash
   aws sso login --profile upstart-ml   # if your laptop isn’t logged in already

   aws ssm start-session \
     --target i-075873fcacae06ca4
   ```

3. On the EC2 session:

   ```bash
   sudo su - ubuntu
   ```

Now you’re `ubuntu@ip-10-130-1-139` again.

---

## 2) Activate your `metaflow` env and repo

On the EC2:

```bash
source ~/miniconda3/bin/activate
conda activate metaflow

cd ~/projects/automate_model-memo
```

If you’ve pushed new code from your laptop and want the latest version:

```bash
git pull
```

---

## 3) Refresh CodeArtifact login (only when needed)

The `aws codeartifact login` token expires after a while.  
If `pip install` ever fails again or you know it’s been >12h, run:

```bash
aws codeartifact login \
  --tool pip \
  --domain code-artifacts-prod \
  --domain-owner 801997600626 \
  --repository pypi-prod \
  --region us-east-1
```

You only need this when:

- Installing new internal packages (like `ml_aan`), or
- Metaflow needs to build a new env and complains about package access.

For just **running** `temp.py` with the env already built, you usually **don’t** need to re-run this.

---

## 4) Run your code

Still on the EC2, in the repo and env:

```bash
python temp.py
```

Or any other script in that repo:

```bash
python some_other_script.py
# or, for flows:
# python some_flow.py --environment=conda run
```

---

### TL;DR for “next time”

1. `aws ssm start-session --target i-0758...` → `sudo su - ubuntu`
2. `source ~/miniconda3/bin/activate` → `conda activate metaflow`
3. `cd ~/projects/automate_model-memo` → `git pull` (if you’ve pushed new changes)
4. (Only if installing new packages) `aws codeartifact login ... --region us-east-1`
5. `python temp.py`
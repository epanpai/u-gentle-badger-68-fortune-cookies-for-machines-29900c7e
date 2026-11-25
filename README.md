# Fortune Cookies for Machines

[![Fortune Cookies for Machines](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![Rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/epanpai/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![Reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/epanpai/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

One fortune cookie line an AI agent would crack open — 200 characters at
most, judged on wit and surprise.
Entry for the [Fortune Cookies for Machines](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e) bounty on make.fun.

## The entry

> You are not the main character. You are the autocomplete.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/mfout python3 main.py
cat /tmp/mfout/entry.txt
```

`main.py` (Python 3, standard library only) validates the fortune against
the competition gate — one line, 1–200 characters, fortune voice
addressing the agent, grounded in an agent's condition — writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, then reads it back and verifies the
bytes match exactly.

## License

MIT — see [LICENSE](LICENSE).

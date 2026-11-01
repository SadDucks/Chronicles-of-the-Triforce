

import json;
from datetime import datetime, timezone;
from pathlib import Path;
import uuid;


class sessionLogger:
    def __init__(self):
        logFolder = Path(__file__).resolve().parent / "GameSessions";
        logFolder.mkdir(parents=True, exist_ok=True);
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f");
        uniqueId = uuid.uuid4().hex[:8];
        self.logFile = logFolder / f"session_{timestamp}_{uniqueId}.jsonl";
        self.logFile.touch(exist_ok=False);
        self.log = [];

    def addLog(self, logEntry):
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event": logEntry if isinstance(logEntry, dict) else {"message": str(logEntry)},
        };
        self.log.append(entry);
        with self.logFile.open("a", encoding="utf-8") as logFile:
            logFile.write(json.dumps(entry, ensure_ascii=True) + "\n");

    def getLog(self):
        return self.log;
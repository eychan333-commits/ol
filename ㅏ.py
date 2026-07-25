<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>턴제 길막기 게임</title>
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        h1 { margin-bottom: 5px; }
        #info {
            font-size: 14px;
            color: #aaa;
            margin-bottom: 15px;
            text-align: center;
        }
        #board {
            display: grid;
            grid-template-columns: repeat(10, 45px);
            grid-template-rows: repeat(10, 45px);
            gap: 4px;
            background-color: #222;
            padding: 10px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        }
        .cell {
            width: 45px;
            height: 45px;
            background-color: #2a2a2a;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            font-weight: bold;
            border-radius: 4px;
            cursor: pointer;
            user-select: none;
            transition: background-color 0.1s;
        }
        .cell:hover {
            background-color: #383838;
        }
        .player { color: #4da6ff; }
        .enemy { color: #ff4d4d; }
        .wall { background-color: #2e7d32; color: #fff; }
        #status {
            margin-top: 15px;
            font-size: 18px;
            font-weight: bold;
            height: 25px;
        }
        #restartBtn {
            margin-top: 15px;
            padding: 10px 20px;
            font-size: 16px;
            background-color: #4da6ff;
            color: #121212;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            display: none;
        }
        #restartBtn:hover {
            background-color: #3399ff;
        }
    </style>
</head>
<body>

    <h1>턴제 길막기 퍼즐</h1>
    <div id="info">
        방향키/WASD: 이동 | 스페이스바: 대기 | 빈 칸 클릭: 장애물 설치<br>
        유령(E)이 당신(@)에게 닿지 않도록 장애물(#)로 길을 막으세요!
    </div>

    <div id="board"></div>
    <div id="status">생존 턴: 0</div>
    <button id="restartBtn" onclick="initGame()">다시 하기</button>

    <script>
        const size = 10;
        let boardData = [];
        let player = { x: 0, y: 0 };
        let enemy = { x: 9, y: 9 };
        let turnCount = 0;
        let isGameOver = false;

        const boardElement = document.getElementById('board');
        const statusElement = document.getElementById('status');
        const restartBtn = document.getElementById('restartBtn');

        function initGame() {
            boardData = Array(size).fill(null).map(() => Array(size).fill(0));
            player = { x: 1, y: 1 };
            enemy = { x: 8, y: 8 };
            turnCount = 0;
            isGameOver = false;
            restartBtn.style.display = 'none';
            render();
        }

        // 유클리드 거리 기반 또는 단순 접근 AI
        function moveEnemy() {
            let dx = player.x - enemy.x;
            let dy = player.y - enemy.y;

            let stepX = dx === 0 ? 0 : dx / Math.abs(dx);
            let stepY = dy === 0 ? 0 : dy / Math.abs(dy);

            let nextX = enemy.x;
            let nextY = enemy.y;

            // 우선순위 정하기 (가까워지는 방향으로 이동 시도)
            if (Math.abs(dx) > Math.abs(dy)) {
                if (boardData[enemy.y][enemy.x + stepX] === 0) {
                    nextX += stepX;
                } else if (boardData[enemy.y + stepY][enemy.x] === 0) {
                    nextY += stepY;
                }
            } else {
                if (boardData[enemy.y + stepY][enemy.x] === 0) {
                    nextY += stepY;
                } else if (boardData[enemy.y][enemy.x + stepX] === 0) {
                    nextX += stepX;
                }
            }

            enemy.x = nextX;
            enemy.y = nextY;
        }

        function playerAction(newX, newY, isWallAction = false) {
            if (isGameOver) return;

            let moved = false;

            if (!isWallAction) {
                // 이동 처리
                if (newX >= 0 && newX < size && newY >= 0 && newY < size) {
                    if (boardData[newY][newX] === 0) {
                        player.x = newX;
                        player.y = newY;
                        moved = true;
                    }
                }
            } else {
                // 벽 설치 처리 (클릭)
                if (boardData[newY][newX] === 0 && !(newX === player.x && newY === player.y) && !(newX === enemy.x && newY === enemy.y)) {
                    boardData[newY][newX] = 1; // 벽
                    moved = true;
                } else {
                    return; // 설치 불가 지역
                }
            }

            if (moved) {
                turnCount++;
                moveEnemy();
                checkGameOver();
                render();
            }
        }

        function checkGameOver() {
            if (player.x === enemy.x && player.y === enemy.y) {
                isGameOver = true;
                statusElement.innerHTML = `<span style="color: #ff4d4d;">게임 오버! 유령에게 잡혔습니다. (생존 턴: ${turnCount})</span>`;
                restartBtn.style.display = 'block';
            } else {
                statusElement.innerText = `생존 턴: ${turnCount}`;
            }
        }

        function render() {
            boardElement.innerHTML = '';
            for (let y = 0; y < size; y++) {
                for (let x = 0; x < size; x++) {
                    const cell = document.createElement('div');
                    cell.classList.add('cell');

                    if (x === player.x && y === player.y) {
                        cell.classList.add('player');
                        cell.innerText = '@';
                    } else if (x === enemy.x && y === enemy.y) {
                        cell.classList.add('enemy');
                        cell.innerText = 'E';
                    } else if (boardData[y][x] === 1) {
                        cell.classList.add('wall');
                        cell.innerText = '#';
                    }

                    // 빈 칸 클릭 시 장애물 설치
                    cell.addEventListener('click', () => {
                        if (!isGameOver) {
                            playerAction(x, y, true);
                        }
                    });

                    boardElement.appendChild(cell);
                }
            }
        }

        // 키보드 입력 처리
        window.addEventListener('keydown', (e) => {
            if (isGameOver) return;

            let nx = player.x;
            let ny = player.y;
            let acted = false;

            switch(e.key) {
                case 'ArrowUp':
                case 'w':
                case 'W':
                    ny--; acted = true; break;
                case 'ArrowDown':
                case 's':
                case 'S':
                    ny++; acted = true; break;
                case 'ArrowLeft':
                case 'a':
                case 'A':
                    nx--; acted = true; break;
                case 'ArrowRight':
                case 'd':
                case 'D':
                    nx++; acted = true; break;
                case ' ': // 스페이스바 (제자리 대기)
                    acted = true; break;
            }

            if (acted) {
                e.preventDefault();
                playerAction(nx, ny, false);
            }
        });

        // 초기 실행
        initGame();
    </script>
</body>
</html>
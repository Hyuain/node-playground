const { exec, spawn } = require('child_process')

// const install = spawn('python', ['-m', 'pip', 'install', 'paddlepaddle', '-i', 'https://mirror.baidu.com/pypi/simple'])
// const install = spawn('cat', ['index.js'])
const install = spawn('pip', ['install', 'paddleocr>=2.0.1', '-i', 'https://mirror.baidu.com/pypi/simple'])
install.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`)
})
install.stdout.on('err', (err) => {
  console.log(`err: ${data}`)
})



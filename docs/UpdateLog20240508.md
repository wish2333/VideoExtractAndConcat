# UpdateLog20240508

优化代码结构，使用asyncio模块实现异步执行FFmpeg命令，使用logging模块实现格式化日志并输出日志

## 修改方向

1. **提高性能效率**：当前代码执行命令后立即等待命令执行完成，这会导致程序在执行命令时出现停滞。如果处理的视频文件较大，或者FFmpeg命令执行时间较长，这将严重影响程序的响应能力。可以考虑使用`asyncio.create_subprocess_exec`异步执行命令，以提高程序的响应性和执行效率。
2. **增强可维护性**：将命令行字符串的构建和执行封装成更具体的函数，比如`execute_cmd`。这样做可以提高代码的可读性和可维护性，同时也方便复用。
3. **日志记录**：目前代码使用`print`函数打印执行的命令和错误信息，这在调试阶段是可行的，但在生产环境中不够灵活。建议引入日志模块（如`logging`），这样可以更方便地控制日志级别，以及将日志输出到不同的地方（如文件、网络等）。
4. **异常处理的改进**：当命令执行失败时，抛出通用的`Exception`可能不是最好的选择。可以定义更具体的异常类，或者根据不同的错误情况抛出不同的异常，这样有助于调用者更准确地处理异常。
5. 优化subprocess代码

## 修改内容

1. class类名修改为FFmpegHandler，需要在main.py中修改
2. logging日志记录
3. 调整为asyncio异步执行
4. 调整debug到新文件

### 修改说明：

1. **安全性问题**：由于使用了异步执行命令`asyncio.create_subprocess_exec`，参数是按位置传递的，这避免了通过字符串拼接构造命令行命令的安全风险。
2. **异常处理**：增加了更详细的异常处理和日志记录，当发生异常时，会记录错误日志并抛出异常，便于问题的定位和解决。
3. **字符编码处理**：在`err.decode('utf-8', errors='ignore')`中增加了`errors='ignore'`参数，用于忽略编码错误，以提高代码的健壮性。
4. **提高性能效率**：通过使用`asyncio`异步执行命令，避免了在执行命令时的阻塞，提高了程序的响应性和执行效率。
5. **增强可维护性**：通过将日志记录引入，替代了直接使用`print`函数，提高了代码的可维护性和日志管理的灵活性。
6. **日志记录**：使用`logging`模块替代`print`进行日志记录，便于管理日志级别和输出。
7. **异常处理的改进**：对异常处理进行了改进，通过记录详细的错误日志并抛出异常，便于调用者根据异常信息进行精确处理。
8. **编码兼容性**：通过使用`asyncio.create_subprocess_exec`和`communicate`，以及合适的错误处理策略，提高了编码的兼容性。

## Debug

debug.py

### 发现问题：asyncio调用错误

如直接调用以下代码会报错

```python
def version(self):
    print(self.run_async(['-version']))
```

原因：由async来def的函数为一个coroutine function，调用时返回coroutine object而不会运行其中的程序

解决：①进入async模式

```python
coro = run_async(['-version'])
asynio.run(coro)
```

②将coroutine变为task

```
await run_async(['-version'])
```

### 发现问题：cmd传入ffmpeg报错

见issue-cmd.log

#### 可能原因，create_subprocess_exec传入错误

https://www.cnblogs.com/lxd670/p/17603616.html

https://www.jianshu.com/p/c7fba094ab42

```python
# 1.源码参数
async def create_subprocess_exec(
  program, 
  *args, 
  stdin=None, 
  stdout=None,
  stderr=None, loop=None,
  limit=streams._DEFAULT_LIMIT, **kwds
)

# 2.调用时入参
asyncio.create_subprocess_exec('ls -l',stdout=asyncio.subprocess.PIPE,stdin=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.PIPE)

# 3.相当于program 指向了 'ls -l'命令
# 4.系统中只有ls、pwd等这些命令，所以'ls -l'这个命令会报错说找不到这个命令文件(FileNotFoundError)
# 5.正确的解法应该是asyncio.create_subprocess_exec('ls', '-l', xxx),把命令和参数分开。
args = cmd.split(' ')
```

还有个问题就是直接在cmd运行、通过subprocess运行都可以在input、output_file路径和filter参数加上引号，但是asyncio不行，因为他是一项一项输入的，不需要引号做划分，这也是个坑点

## 进度

- [x] 对version函数的修改
- [x] 对extract函数的修改
  - [x] async def get_duration
  - [x] asyncio.run(run_async())
- [x] 对merge函数的修改
- [x] 处理overwrite事件（默认覆盖-y或不覆盖-n）

## 下一步修改目标

- [ ] overwrite选项UI实现
- [ ] 双文件合并选项核心逻辑实现、UI实现
- [ ] UI重构，为后续功能预留空间
  - [ ] 源代码链接
  - [ ] Browse同步textEdit
  - [ ] 每个功能一栏
- [ ] 后续功能预想
  - [ ] 单文件、多文件转码
  - [ ] 编码格式选项实现

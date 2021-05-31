# Pytest<br/>
## 1.pytest用例的执行方式<br/>
(1)命令行方式直接用pytest执行<br/>
pytest [-vs] [filename]<br/>
-v:显示用例执行的详细信息
[filename]运行指定的文件如果不加默认运行所有命名符合规则的文件。<br/>
Tips:如果只执行 pytest ，会查找当前目录及其子目录下以  test_*.py  或 *_test.py 文件，找到文件后，在文件中找到以  test 开头函数并执行。<br/>
列子:<br/>
![](.Readme_images/589c7cb0.png)<br/>
如果只以pytest执行就会看到所有用例全部被执行。<br/>
![](.Readme_images/a647d28e.png)<br/>
可以看到我这里加上了具体的文件路径就执行了对应的测试。<br/>
(2)main函数方式<br/>
```python
import pytest

if __name__ == '__main__':
    pytest.main(['-v','automation/test_fixtureuse.py'])

```
(3)在pytest.ini文件中配置textpaths<br/>
pytest默认是搜索执行当前目录下的所有用例，当pytest.ini配置了testpaths = test_case/lxk或testpaths = test_case/lxk/test_001_case.py就会只执行当前配置的文件夹下或文件里的用例，这样我们就可以灵活的控制运行需要测试的用例了，可配置多个，空格隔开<br/>
例子:<br/>
testpaths = automation/test_square.py<br/>

### pytest command扩充 <br/>
运行某个模块里面的某个函数，或者某个类，某个类里面的方法.<br/>
```
pytest -v [filename].py::[TestClass]::[Testmethod]
```
```python
class TestClass():
    flag = 1
    def test_gg1(self):
        print('gg')
    assert flag == 1

def test_login2(login):
    flag = 1
    print('调用login')
    assert flag==1
```
![](.README_images/bcf567b5.png)
![](.README_images/e26c5668.png)
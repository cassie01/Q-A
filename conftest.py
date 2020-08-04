import pytest
import smtplib
from email.mime.text import MIMEText
from email.header import Header


@pytest.fixture(scope="function", autouse=True)
def foo():
    print("function started")
    yield 100
    print('function end')

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    print('------------------------------------')

    # 获取钩子方法的调用结果
    out = yield
    print('用例执行结果', out)

    # 3. 从钩子方法的调用结果中获取测试报告
    report = out.get_result()

    print('测试报告：%s' % report)
    print('步骤：%s' % report.when)
    print('nodeid：%s' % report.nodeid)
    print('description:%s' % str(item.function.__doc__))
    print(('运行结果: %s' % report.outcome))

def pytest_sessionstart(session):
    session.results = dict()



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    # print(result)
#所有测试结果都存储在session.resultsdict 下
    if result.when == 'call':
        item.session.results[item] = result

# global message_content
def pytest_sessionfinish(session, exitstatus):
    print()
    # print('run status code:', exitstatus)
    print(session)
    passed_amount = sum(1 for result in session.results.values() if result.passed)
    failed_amount = sum(1 for result in session.results.values() if result.failed)
    message_content = (f'there are {passed_amount} passed and {failed_amount} failed tests')
    print(message_content)
    return message_content

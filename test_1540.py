import pytest

def inc(x):
    return x+1

# def setup_function():
#     print("started。。。。。。。。。。。。。")
#
# def teardown_function():
#     print("ending。。。。。。。。。。。。。")
# @pytest.mark.answer
def test_answer_1():
    print('tag==001')
# @pytest.mark.answer
def test_answer_2(foo):
    print(foo)
    assert inc(98) == foo

if __name__ == '__main__':
    pytest.main()

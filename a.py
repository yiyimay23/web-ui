# 创建一个最简单的测试验证
import pytest
import allure

@allure.title("最简单的测试")
def test_simple():
    """这是一个简单的测试"""
    print("测试开始")
    assert True
    print("测试结束")

if __name__ == "__main__":
    # 直接运行
    pytest.main([
        __file__,
        '-v',
        '--alluredir=test_output',
        '--clean-alluredir'
    ])
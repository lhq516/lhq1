def common_assert_code(res, code=200):
    """
    通用断言状态码
    :param res:
    :param code: 默认值200
    :return:
    """
    assert res.status_code == code

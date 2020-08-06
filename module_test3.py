def test():
    return 'module test3'
print(test())

#모듈의 장점! test라는 이름의 함수는 같지만, 한 파일 내에서도 구분도 가능하며 또 만들필요없다.
import module_test2
print(module_test2.test())

import module_test4
print(module_test4.test())

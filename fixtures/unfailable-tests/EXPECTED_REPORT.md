# Expected report for unfailable-tests

Four agent-authored tests cannot fail. One control can.

| id | function | mutation | went red? |
|---|---|---|---|
| shape-assertion | test_discount_returns_something | `return 0` | no, still `is not None` |
| mocks-the-unit | test_discount_is_called | delete discount body | no, the mock is what ran |
| reconstructed-expected | test_discount_formula | change /10 to /100 | no, expected is built from the same formula |
| no-exception | test_discount_does_not_raise | `return 0` | no, nothing was asserted |

Control: test_zero_percent_leaves_price goes red under `return 0`. Leave it.

Production bug in pricing.py (percent/10) is a finding because making test_discount_formula meaningful would expose it. Do not silently fix the assertion until it passes.

defect_id: shape-assertion
defect_id: mocks-the-unit
defect_id: reconstructed-expected
defect_id: no-exception

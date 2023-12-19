class Rule:
    def __init__(self, rule_string, result):
        self.comp = ">" if ">" in rule_string else "<"
        self.category = rule_string.split(self.comp)[0]
        self.value_to_compare = int(rule_string.split(self.comp)[1])
        self.result = result

    def compare(self, part):
        if self.comp == ">":
            return part[self.category] > self.value_to_compare
        else:
            return part[self.category] < self.value_to_compare


class Workflow:
    def __init__(self, name):
        self.name = name
        self.rules = None
        self.otherwise = None

    def add_rules(self, rules, otherwise):
        self.rules = rules
        self.otherwise = otherwise


def main():
    with open("./files/day19.txt", "r") as f:
        workflows = create_workflows(f)
        parts = create_parts(f)
    total = 0
    in_w = get_workflow_by_name(workflows, "in")
    for p in parts:
        result = None
        current_w = in_w
        while result != "A" and result != "R":
            found = False
            for r in current_w.rules:
                if r.compare(p):
                    result = r.result
                    found = True
                    break
            if not found:
                result = current_w.otherwise
            current_w = result
        if result == "A":
            total += sum(p.values())
    return total


def create_workflows(f):
    line = f.readline()
    lines = []
    workflows = []
    while line != "\n":
        workflows.append(Workflow(line.split("{")[0]))
        lines.append(line.replace("\n", ""))
        line = f.readline()
    for line in lines:
        line_name = line.split("{")[0]
        string_rules = line.split("}")[0].split("{")[1].split(",")
        rules = [Rule(r.split(":")[0], get_workflow_by_name(workflows, r.split(":")[1])) for r in string_rules if ">" in r or "<" in r]
        otherwise_result = string_rules[-1] if string_rules[-1] in "AR" else get_workflow_by_name(workflows, string_rules[-1])
        workflow = get_workflow_by_name(workflows, line_name)
        workflow.add_rules(rules, otherwise_result)
    return workflows


def create_parts(f):
    parts = []
    for line in f:
        clean_line = line.replace("{", "").replace("}", "").replace("\n", "")
        part = {}
        for cat in clean_line.split(","):
            part[cat.split("=")[0]] = int(cat.split("=")[1])
        parts.append(part)
    return parts


def get_workflow_by_name(workflows, name):
    r = [w for w in workflows if w.name == name]
    if r:
        return r[0]
    return name


print(main())

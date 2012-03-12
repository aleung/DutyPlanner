#!/usr/bin/env python

import itertools
import input

class Group:
	def __init__(self, staffs):
		self.staffs = staffs
		# {staff_name, role}
		self.members = {}

	def set_member(self, role, staff):
		if staff in self.members.keys():
			raise ValueError
		self.members[staff] = role

	def get_members(self):
		return self.members

	def get_competence(self, area):
		competences = [self.staffs[name]['competence'][area] for name in self.members.keys()]
		return max(competences)

class GroupBuilder():
	def __init__(self, staffs, group_definition):
		self.staffs = staffs
		self.group_definition = group_definition
		self.groups = []

	def build(self):
		number_persons_in_group = sum(map(lambda r : r[1] , self.group_definition['roles']))
		for staff_combination in itertools.combinations(self.staffs.keys(), number_persons_in_group):
			self.build_groups(staff_combination)
		return self.groups

	def build_groups(self, staff_combination):
		combination_of_each_roles = []
		for number_persons in map(lambda r : r[1] , self.group_definition['roles']):
			combination_of_each_roles.append(list(itertools.combinations(staff_combination, number_persons)))
		for cartesian_product in itertools.product(*combination_of_each_roles):
			self.build_a_group([ staff for t in cartesian_product for staff in t ])

	def build_a_group(self, members_in_a_group):
		group = Group(self.staffs)
		for (role, number_persons_in_group) in self.group_definition['roles']:
			for i in range(number_persons_in_group):
				try:
					group.set_member(role, members_in_a_group.pop(0))
				except ValueError:
					return
		if self.validate_group(group):
			self.groups.append(group)

	def validate_group(self, group):
		competence_requirement = self.group_definition['competence_requirement']
		for area in competence_requirement.keys():
			if group.get_competence(area) < competence_requirement[area]:
				return False
		return True


if __name__ == "__main__":
	pass
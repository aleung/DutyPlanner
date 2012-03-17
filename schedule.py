#!/usr/bin/env python

import itertools
import input


class Group:
	def __init__(self, staffs):
		self.staffs = staffs
		# {staff_name : role}
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


class ScheduleBuilder():
	def __init__(self, groups, number_of_iterations, schedule_exclude, max_continuous_iterations):
		self.groups = groups
		self.number_of_iterations = number_of_iterations
		self.schedule_exclude = schedule_exclude
		self.max_continuous_iterations = max_continuous_iterations
		self.schedules = []

	def build(self):
		for schedule in itertools.permutations(self.groups, self.number_of_iterations):
			if self.validate_schedule(schedule):
				self.schedules.append(schedule)
		return self.schedules

	def validate_schedule(self, schedule):
		for i in range(self.number_of_iterations):
			exclude_staffs = set([ name for (iteration, name) in self.schedule_exclude if iteration == i ])
			if exclude_staffs.intersection(schedule[i].get_members().keys()):
				return False
			if i >= self.max_continuous_iterations:
				for member in schedule[i].get_members().keys():					
					for prev in range(self.max_continuous_iterations):
						if member in schedule[i-prev].get_members().keys:
							return False
		return True


class SchedulePrinter():
	def __init__(self):
		pass

	def print_schedule(self, schedule):
		for num in range(len(schedule)):
			print "Iteration " + num
			print schedule[num].get_members
		pass #TODO


if __name__ == "__main__":
	groups = GroupBuilder(input.staffs, input.group_definition).build()
	print "%d group options available." % len(groups)
	schedules = ScheduleBuilder(groups, len(input.iteration_days), input.schedule_exclude, input.max_continuous_iterations).build()
	printer = SchedulePrinter()
	for schedule in schedules:
		printer.print_schedule(schedule)
	pass

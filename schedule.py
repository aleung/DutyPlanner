#!/usr/bin/env python

import itertools
import input


class Group:
	def __init__(self, staffs):
		self.staffs = staffs
		# {staff_name : role}
		self.members = {}

	def set_member(self, staff, role):
		if staff in self.members.keys():
			raise ValueError
		self.members[staff] = role

	def get_members(self):
		return self.members

	def get_competence(self, area):
		competences = [self.staffs[name]['competence'][area] for name in self.members.keys()]
		return max(competences)

	def __repr__(self):
		return "Group: %s" % self.members


class GroupBuilder():
	def __init__(self, staffs, group_definition):
		self.staffs = staffs
		self.group_definition = group_definition
		self.qualified_groups = []

	def build(self):
		number_persons_in_group = sum(map(lambda r : r[1] , self.group_definition['roles']))
		for staff_combination in itertools.combinations(self.staffs.keys(), number_persons_in_group):
			self.__build_groups(staff_combination)
		return self.qualified_groups

	def __build_groups(self, staff_combination):
		combination_of_each_roles = []
		for number_persons in map(lambda r : r[1] , self.group_definition['roles']):
			combination_of_each_roles.append(list(itertools.combinations(staff_combination, number_persons)))
		for cartesian_product in itertools.product(*combination_of_each_roles):
			self.__build_a_group([ staff for t in cartesian_product for staff in t ])

	def __build_a_group(self, members_in_a_group):
		group = Group(self.staffs)
		for (role, number_persons_in_group) in self.group_definition['roles']:
			for i in range(number_persons_in_group):
				try:
					group.set_member(members_in_a_group.pop(0), role)
				except ValueError:
					return
		if self.__validate_group_competence(group):
			self.qualified_groups.append(group)

	def __validate_group_competence(self, group):
		competence_requirement = self.group_definition['competence_requirement']
		for area in competence_requirement.keys():
			if group.get_competence(area) < competence_requirement[area]:
				return False
		return True


class IterationGroupCandidatesBuilder:
	def __init__(self, qualified_groups):
		self.qualified_groups = qualified_groups

	def build_candidate_groups_for_iterations(self, iterations_definition):
		groups_in_iterations = []
		for iteration in iterations_definition:
			groups_in_iterations.append(self.__get_candidate_groups(iteration['pre_plan']))
		return groups_in_iterations

	def __get_candidate_groups(self, pre_plan):
		groups = []
		for group in self.qualified_groups:
			if self.__does_group_meet_pre_plan(group, pre_plan):
				groups.append(group)
		return groups

	def __does_group_meet_pre_plan(self, group, pre_plan):
		for pre_plan_member in pre_plan:
			if pre_plan[pre_plan_member] == 'NA':
				if pre_plan_member in group.get_members():
					return False
			else:
				if pre_plan_member not in group.get_members():
					return False
				if pre_plan[pre_plan_member] != group.get_members()[pre_plan_member]:
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
				for member in schedule[i].get_members():					
					for prev in range(self.max_continuous_iterations):
						if member in schedule[i-prev].get_members():
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

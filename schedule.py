#!/usr/bin/env python

import itertools
import random
import datetime
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

	def get_role_competence(self, role, area):
		competences = [self.staffs[name]['competence'][area] for name in self.members.keys() if self.members[name] == role]
		return max(competences)

	def __repr__(self):
		return "Group: %s" % self.members


class GroupBuilder():
	def __init__(self, staffs, group_definition):
		self.staffs = staffs
		self.group_definition = group_definition
		self.qualified_groups = []

	def build(self):
		number_persons_in_group = sum(self.__get_number_persons_roles())
		for staff_combination in itertools.combinations(self.staffs.keys(), number_persons_in_group):
			self.__build_groups(staff_combination)
		return self.qualified_groups

	def __get_role_list(self):
		return self.group_definition['roles'].keys()

	def __get_number_persons_roles(self):
		return [self.group_definition['roles'][name]['persons'] for name in self.__get_role_list()]

	def __build_groups(self, staff_combination):
		combination_of_each_roles = []
		for number_persons in self.__get_number_persons_roles():
			combination_of_each_roles.append(list(itertools.combinations(staff_combination, number_persons)))
		for cartesian_product in itertools.product(*combination_of_each_roles):
			self.__build_a_group([ staff for t in cartesian_product for staff in t ])

	def __build_a_group(self, members_in_a_group):
		group = Group(self.staffs)
		for role in self.__get_role_list():
			for i in range(self.group_definition['roles'][role]['persons']):
				try:
					group.set_member(members_in_a_group.pop(0), role)
				except ValueError:
					return
		if self.__validate_group_competence(group):
			self.qualified_groups.append(group)

	def __validate_group_competence(self, group):
		for role in self.__get_role_list():
			role_competence_requirement = self.group_definition['roles'][role]['competence_requirement']
			if not self.__validate_competence(role_competence_requirement, lambda area : group.get_role_competence(role, area)):
				return False
		return self.__validate_competence(self.group_definition['competence_requirement'], lambda area : group.get_competence(area))

	def __validate_competence(self, competence_requirement, get_competence):
		for area in competence_requirement.keys():
			if get_competence(area) < competence_requirement[area]:
				return False
		return True


class IterationGroupCandidatesBuilder:
	def __init__(self, qualified_groups):
		self.qualified_groups = qualified_groups

	def build(self, iterations_definition):
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
	def __init__(self, groups_in_iterations):
		self.groups_in_iterations = groups_in_iterations
		self.schedule = []

	def build(self):
		self.__shuffle_groups()
		if self.__schedule_iteration(0):
			return self.schedule
		else:
			return None

	def __schedule_iteration(self, iteration_id):
		''' Returns: True - solution found; False - unable to schedule '''
		if iteration_id == len(groups_in_iterations):
			return True
		for group in self.groups_in_iterations[iteration_id]:
			if not self.__is_group_overload(group, iteration_id):
				self.schedule.append(group)
				if self.__schedule_iteration(iteration_id + 1):
					return True
				else:
					self.schedule.pop()
		return False

	def __shuffle_groups(self):
		for i in range(len(self.groups_in_iterations)):
			random.shuffle(groups_in_iterations[i])

	def __is_group_overload(self, group, iteration_id):
		if iteration_id == 0:
			return False
		prev_iteration_members = set(self.schedule[iteration_id - 1].get_members().keys())
		return prev_iteration_members.intersection(group.get_members().keys())



class SchedulePrinter():
	def __init__(self, schedule, iterations_definition, begin_date, staffs):
		self.schedule = schedule
		self.iterations_definition = iterations_definition
		self.begin_date = begin_date
		self.staffs = staffs

	def print_schedule(self):
		if self.schedule == None:
			print "No way to schedule."
			return
		self.__print_header()
		from_date = self.begin_date
		for i in range(len(self.schedule)):
			to_date = from_date + datetime.timedelta(days=self.iterations_definition[i]['days']-1)
			self.__print_iteration(from_date, to_date, i)
			from_date += datetime.timedelta(days=self.iterations_definition[i]['days'])

	def __print_header(self):
		output = '|'.rjust(25)
		for staff in self.staffs:
			output += ' %10s |' % staff
		print output

	def __print_iteration(self, from_date, to_date, iteration):
		output = '%s - %s |' % (str(from_date), str(to_date))
		for staff in self.staffs:
			preplanned = staff in self.iterations_definition[iteration]['pre_plan']

			if staff in self.schedule[iteration].get_members():
				output += ' %10s |' % (('* ' if preplanned else '') + self.schedule[iteration].get_members()[staff])
			else:
				output += (('* ' if preplanned else '') + '|').rjust(13)
		print output


if __name__ == "__main__":
	groups = GroupBuilder(input.staffs, input.group_definition).build()
	print "%d group options available." % len(groups)
	groups_in_iterations = IterationGroupCandidatesBuilder(groups).build(input.iterations_definition)

	for i in range(len(input.iterations_definition)):
		print "Iteration #%i - %i candidate groups." % (i, len(groups_in_iterations[i]))

	print

	schedule = ScheduleBuilder(groups_in_iterations).build()
	printer = SchedulePrinter(schedule, input.iterations_definition, input.iteration_begin_date, input.staffs)
	printer.print_schedule()

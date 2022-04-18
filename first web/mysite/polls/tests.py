
from http import client
from time import time
from urllib import response
from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
import datetime
from .models import Question , Choice


class QuestionModelTests(TestCase):

    def test_recently_published_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        return self.assertIs(future_question.recently_published() ,False)

    def test_for_question_older_than_one_days(self):
        time = timezone.now() - datetime.timedelta(days=1 , seconds=1)
        older_question = Question(pub_date=time)

        return self.assertIs(older_question.recently_published() ,False)


    def test_for_question_published_very_recent(self):
        time= timezone.now() - datetime.timedelta(hours=23 ,minutes=59 , seconds=59)
        recent_question = Question(pub_date = time)

        return self.assertIs(recent_question.recently_published() , True)


def create_question(question_text,days):
    time= timezone.now()+datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,pub_date= time)


class QuestionIndexViewsTest(TestCase):
    
    def test_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'] ,[])




    def test_past_question(self):
        question = create_question(question_text = 'past question.' , days= -30)
        response = self.client.get(reverse('polls:index'))

        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )
    
    def test_past_two_question(self):

        question1=create_question(question_text= "past question 1." ,days= -30)
        question2 = create_question(question_text = 'past question 2.' , days = -5)

        response = self.client.get(reverse('polls:index'))

        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2,question1],
        )


class QuestionDetailViewTests(TestCase):

    def test_future_question(self):
        future_question = create_question(question_text="Future question" , days=5)
        response = self.client.get(reverse('polls:detail' , args=(future_question.id,)) )
        self.assertEqual(response.status_code,404)



    def test_past_question(self):
        past_question = create_question(question_text="past question" , days=-5)
        response= self.client.get(reverse('polls:detail' , args=(past_question.id,)))

        self.assertContains(response,past_question.question_text)


class QuestionResultViewTests(TestCase):

    def test_future_question(self):
        future_question= create_question(question_text="Future Question" , days=30)
        response= self.client.get(reverse('polls:results' , args=(future_question.id,)))

        self.assertEqual(response.status_code,404)


    def test_past_question(self):
        past_question = create_question(question_text="Past Question", days=-5)
        response = self.client.get(reverse('polls:results' , args=(past_question.id,)))

        self.assertContains(response,past_question.question_text)



def create_choice(question_text,days,choice_text=0):
    question = create_question(question_text,days)
    if choice_text:
        question.choice_set.create(choice_text= choice_text,vote= 0)
        return question

    else:
        return question


class ChoiceResultTests(TestCase):

    def test_no_choice(self):
        question = create_choice(question_text='question with no choice' , days=-2)
        response= self.client.get(reverse('polls:results' , args=(question.id,) ))

        self.assertEqual(question.choice_set.count(),0)
        self.assertQuerysetEqual(question.choice_set.all(),[])

    def test_with_choice(self):
        question = create_choice(question_text='with choice' , days=-1,choice_text='hello')
        self.assertEqual(question.choice_set.count() , 1)












        








        









